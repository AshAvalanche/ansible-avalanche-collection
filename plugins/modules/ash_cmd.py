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


# Check if the command is valid for the CLI
# Also check if the command triggers a transaction
def check_command(module: AnsibleModule, command: list()) -> (bool, bool):
    # If the command is valid, then the help command should return 0
    help_command = command.copy()
    help_command.append("--help")
    help_result = module.run_command(" ".join(help_command))
    if help_result[0] > 0:
        return False, False

    # If the command triggers a transaction, then the version command contains 'tx_cmd=true'
    tx_cmd_regex = r"tx_cmd=(true|false)"
    version_command = command.copy()
    version_command.append("--version")
    version_result = module.run_command(" ".join(version_command))
    tx_cmd = re.search(tx_cmd_regex, version_result[1])
    if tx_cmd:
        if tx_cmd.group(1) == "true":
            return True, True
        else:
            return True, False

    return True, False


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
    flag_regex = r" --?\w+"
    if re.search(flag_regex, " ".join(module.params["command"])):
        module.fail_json(
            msg="The command parameter can not contain options or flags. Please use the 'options' parameter.",
            **result,
        )

    # Build the command
    command = [module.params["ash_path"]] + module.params["command"]

    # Check if the command is valid
    valid, transaction = check_command(module, command)
    if not valid:
        module.fail_json(
            msg=f"'{command}' is not a valid command.",
            command=" ".join(command),
            **result,
        )

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

    # If the command triggered a transaction, then set changed to true
    if transaction:
        result['changed'] = True

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
