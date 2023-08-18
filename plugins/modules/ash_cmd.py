#!/usr/bin/python

# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2023, E36 Knots

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import re

from ansible.module_utils.basic import AnsibleModule

FORBIDDEN_FLAGS = [
    "config",
    "json",
    "private-key",
    "help",
    "version",
]


def run_module():
    # Define module arguments
    module_args = dict(
        command=dict(type="list", required=True),
        options=dict(type="dict", required=False, default={}),
        ash_path=dict(
            type="str", required=False, default="/opt/avalanche/ash-cli/bin/ash"
        ),
        ash_config=dict(
            type="str",
            required=False,
            default="/etc/avalanche/ash-cli/conf/default.yml",
        ),
        avalanche_private_key=dict(type="str", required=False, no_log=True),
        json=dict(type="bool", required=False, default=True),
    )

    # Define result argument
    result = dict(changed=False)

    # Create the module instance
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    # Fail if there are flags/options in the command variable
    # Regex to match flags/options
    regex = r" --?\w+"
    if re.search(regex, " ".join(module.params["command"])):
        module.fail_json(
            msg="The command parameter can not contain options or flags. Please use the 'options' parameter.",
            **result,
        )

    # Build the command
    command = [module.params["ash_path"]] + module.params["command"]

    # Add the params
    for key, value in module.params["options"].items():
        # If key is in FORBIDDEN_FLAGS, then fail
        if key in FORBIDDEN_FLAGS:
            module.fail_json(
                msg="Passing '{}' as an option is not allowed. Please use the appropriate parameter.".format(
                    key
                ),
                **result,
            )
        # If value is boolean false, then skip
        if value is False:
            continue
        command.append("--" + key)
        # If value is boolean true, then it's a flag
        if value is True:
            continue
        # If value is int, cast to string
        if isinstance(value, int):
            value = str(value)
        # If value is float, cast to string
        if isinstance(value, float):
            value = str(value)
        command.append(value)

    # Add the private key
    if module.params["avalanche_private_key"]:
        command.append("--private-key")
        command.append(module.params["avalanche_private_key"])

    # Force json output
    if module.params["json"]:
        command.append("--json")

    # Add the config flag
    command.append("--config")
    command.append(module.params["ash_config"])

    # Run the command
    run = module.run_command(" ".join(command))

    # Exit with failure if rc is not 0
    if run[0] > 0:
        module.fail_json(
            msg=run[2],
            command=" ".join(command),
            **result,
        )

    # TODO: act on result['changed'] when the cli will perform transactions
    # Result['changed'] = True

    # Save the command that was executed
    result["command"] = " ".join(command)

    # Save the json output from stdout
    result["output"] = json.loads(run[1])

    # Exit with the result if there was no error
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
