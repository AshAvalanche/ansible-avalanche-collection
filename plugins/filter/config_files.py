#!/usr/bin/python
# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2025, E36 Knots

"""Plan how the file paths referenced in a config mapping are made available on
the target host. Generic and role-agnostic: any role declares which of its
config keys hold file/directory paths (and the default host path for each) and
reuses this filter together with the ``config_files`` role that runs the plan.

``config_file_plan(config, fields)``

* ``config`` - the parsed config mapping (returned rewritten, never mutated).
* ``fields`` - list of descriptors declaring the affected keys::

      - path: "server.tls.certFile"   # dotted path; "[]" iterates a list
        dest: "/etc/erpc/tls/cert.pem" # DEFAULT path on the host for this key
        type: file                     # file | dir
        mode: "0644"                   # mode applied to copied files

For every affected key that is present in the config, its value decides what
happens (and the value is rewritten so the deployed config is valid on the host):

* a plain **string** -> a path ON THE CONTROLLER. It is copied to the field's
  default ``dest`` and the value is rewritten to ``dest``. (action ``copy``)
* a mapping ``{src, dst}`` -> ``dst`` overrides the destination; ``src`` (on the
  controller) is copied to ``dst`` and the value is rewritten to ``dst``.
  ``src`` is mandatory when ``dst`` is given. (action ``copy``)
* a mapping ``{path}`` -> nothing is copied; ``path`` must already exist on the
  host (a file must exist, a directory must exist and be non-empty) and the value
  is rewritten to ``path``. (action ``verify``)
* anything else -> an error.

Returns ``{"config": <rewritten>, "operations": [<op>...]}`` where each op is
``{action, addr, type, dest[, src, mode]}``.
"""

import copy

from ansible.errors import AnsibleFilterError


def _slots(node, tokens, addr):
    """Yield ``(container, key, addr)`` for every leaf the dotted path reaches."""
    token = tokens[0]
    rest = tokens[1:]

    if token == "[]":
        if isinstance(node, list):
            for index, item in enumerate(node):
                for slot in _slots(item, rest, "%s[%d]" % (addr, index)):
                    yield slot
        return

    if not isinstance(node, dict) or token not in node:
        return

    child_addr = (addr + "." + token) if addr else token
    if rest:
        for slot in _slots(node[token], rest, child_addr):
            yield slot
    else:
        yield node, token, child_addr


def _classify(value, addr, dest, ftype, mode):
    """Return ``(operation_or_None, new_value)`` for one affected key value."""
    if isinstance(value, str):
        # Empty or a ${VAR} placeholder is left untouched.
        if value == "" or value.startswith("${"):
            return None, value
        op = {"action": "copy", "addr": addr, "type": ftype,
              "src": value, "dest": dest, "mode": mode}
        return op, dest

    if isinstance(value, dict):
        keys = set(value.keys())
        if "dst" in keys:
            if keys != {"src", "dst"}:
                raise AnsibleFilterError(
                    "config_file_plan: '%s' with 'dst' must hold exactly "
                    "{src, dst} (got %s)" % (addr, sorted(keys))
                )
            op = {"action": "copy", "addr": addr, "type": ftype,
                  "src": value["src"], "dest": value["dst"], "mode": mode}
            return op, value["dst"]
        if keys == {"path"}:
            op = {"action": "verify", "addr": addr, "type": ftype,
                  "dest": value["path"]}
            return op, value["path"]
        raise AnsibleFilterError(
            "config_file_plan: '%s' must be a path string, {src, dst} or "
            "{path} (got keys %s)" % (addr, sorted(keys))
        )

    raise AnsibleFilterError(
        "config_file_plan: '%s' must be a string or a mapping (got %r)"
        % (addr, type(value).__name__)
    )


def config_file_plan(config, fields):
    if not isinstance(config, dict):
        raise AnsibleFilterError("config_file_plan: the config must be a mapping")
    if not isinstance(fields, list):
        raise AnsibleFilterError("config_file_plan: fields must be a list")

    cfg = copy.deepcopy(config)
    operations = []
    seen = set()

    for field in fields:
        path = field.get("path")
        dest = field.get("dest")
        if not path or not dest:
            raise AnsibleFilterError(
                "config_file_plan: every field needs a 'path' and a 'dest'"
            )
        ftype = field.get("type", "file")
        mode = str(field.get("mode", "0644"))
        tokens = path.replace("[]", ".[]").strip(".").split(".")

        for container, key, addr in _slots(cfg, tokens, ""):
            op, new_value = _classify(container[key], addr, dest, ftype, mode)
            container[key] = new_value
            if op is None:
                continue
            signature = (op["action"], op.get("src"), op["dest"], op["type"])
            if signature in seen:
                continue
            seen.add(signature)
            operations.append(op)

    return {"config": cfg, "operations": operations}


class FilterModule(object):
    def filters(self):
        return {"config_file_plan": config_file_plan}
