#!/usr/bin/python
# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2025, E36 Knots

"""Extract the backend upstreams an eRPC configuration talks to.

Given a parsed eRPC config (mapping), ``erpc_backends`` returns one entry per
upstream endpoint:

  ``{"project", "alias", "endpoint"}``

where ``project`` is the project id, ``alias`` is True when a wildcard
``server.aliasing`` rule serves that project's EVM chains at the URL root
(``<base>/<chainId>``) rather than the canonical
``<base>/<project>/evm/<chainId>``, and ``endpoint`` is the backend RPC URL.

The role queries each endpoint for its ``eth_chainId`` so it can print the real
numeric chainIds (and therefore the reachable routes) at the end of the run.
"""

from ansible.errors import AnsibleFilterError

ARCHITECTURE = "evm"


def _has_root_alias(aliasing, pid):
    """True when a wildcard alias serves <pid>/evm at the URL root."""
    for rule in aliasing:
        if not isinstance(rule, dict) or rule.get("serveProject") != pid:
            continue
        if rule.get("serveArchitecture") not in (None, ARCHITECTURE):
            continue
        if rule.get("matchDomain", "*") in ("*", None):
            return True
    return False


def erpc_backends(config):
    if not isinstance(config, dict):
        raise AnsibleFilterError("erpc_backends: the config must be a mapping")

    server = config.get("server") or {}
    aliasing = (server.get("aliasing") or {}).get("rules") or []
    out = []

    for project in config.get("projects") or []:
        if not isinstance(project, dict):
            continue
        pid = project.get("id", "main")
        root_alias = _has_root_alias(aliasing, pid)
        for upstream in project.get("upstreams") or []:
            if not isinstance(upstream, dict):
                continue
            endpoint = upstream.get("endpoint")
            if endpoint:
                out.append({
                    "project": pid,
                    "alias": root_alias,
                    "endpoint": endpoint,
                })

    return out


class FilterModule(object):
    def filters(self):
        return {"erpc_backends": erpc_backends}
