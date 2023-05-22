#!/usr/bin/python

# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2023, E36 Knots

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import subprocess
import json

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define module arguments
    module_args = dict(
        command=dict(type="str", required=True),
        options=dict(type="dict", required=False, default={}),
        ash_path=dict(type="str", required=False, default="/usr/local/bin/ash"),
        json=dict(type="bool", required=False, default=True),
    )

    # define result argument
    result = dict(changed=False)

    # create the module instance
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    # stop here if there are flags/options in the command variable
    if module.params["command"].find("--") != -1:
        module.fail_json(
            msg="The command parameter can not contain options or flags, please use the options parameter",
            **result
        )

    # build the command from the params
    command = [module.params["ash_path"], module.params["command"]]
    for key, value in module.params["options"].items():
        command.append("--" + key)
        # if value is boolean true, then it's a flag:
        if value is True:
            continue
        # if value is int, cast to string
        if isinstance(value, int):
            value = str(value)
        command.append(value)
    # force json output
    if module.params["json"]:
        command.append("--json")

    # run the command
    run = subprocess.run(" ".join(command), capture_output=True, shell=True)

    # exit with failure if there was an execution error
    if run.stderr:
        module.fail_json(msg=run.stderr, **result)

    # TODO: act on result['changed'] when the cli will perform transactions
    # result['changed'] = True

    # save the json output
    result["output"] = json.loads(run.stdout)

    # exit with the result if there was no error
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
