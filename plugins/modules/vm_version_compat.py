#!/usr/bin/python

# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2024, E36 Knots

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import Request

GITHUB_RAW_URL = "https://raw.githubusercontent.com"
GITHUB_API_URL = "https://api.github.com"

def get_json(url):
    r = Request()

    return json.loads(r.get(url).read())


def run_module():
    # Define module arguments
    module_args = dict(
        vm_gh_repo=dict(type="str", required=True),
        vm_version=dict(type="str", required=True),
        avalanche_gh_repo=dict(type="str", required=True),
        avalanche_version=dict(type="str", required=True),
        strict=dict(type="bool", required=False, default=False),
    )

    # Define result argument
    result = dict(changed=False)

    # Create the module instance
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    vm_repo = module.params["vm_gh_repo"]
    vm_version = module.params["vm_version"]
    avax_repo = module.params["avalanche_gh_repo"]
    avax_version = module.params["avalanche_version"]

    vm_compat_json_url = f"{GITHUB_RAW_URL}/{vm_repo}/{vm_version}/compatibility.json"
    avax_compat_json_url = (
        f"{GITHUB_RAW_URL}/{avax_repo}/{avax_version}/version/compatibility.json"
    )

    try:
        vm_compat_json = get_json(vm_compat_json_url)
    except Exception as e:
        module.fail_json(
            msg=f"Failed to get compatibility JSON at {vm_compat_json_url}: {e}"
        )

    try:
        avax_compat_json = get_json(avax_compat_json_url)
    except Exception as e:
        module.fail_json(
            msg=f"Failed to get compatibility JSON at {avax_compat_json_url}: {e}"
        )

    vm_rpcchainvm_proto_version = int(
        vm_compat_json["rpcChainVMProtocolVersion"][vm_version]
    )
    formated_avax_version = avax_version.replace("-fuji", "")
    for rpc_ver, avax_ver in avax_compat_json.items():
        if formated_avax_version in avax_ver:
            avax_rpcchainvm_proto_version = int(rpc_ver)
            break

    if "avax_rpcchainvm_proto_version" not in locals():
        module.fail_json(
            msg=f"AvalancheGo version {avax_version} not found in compatibility JSON:\n{avax_compat_json_url}"
        )

    result["vm_rpcchainvm_proto_version"] = vm_rpcchainvm_proto_version
    result["avalanche_rpcchainvm_proto_version"] = avax_rpcchainvm_proto_version
    result["is_compatible"] = (
        vm_rpcchainvm_proto_version == avax_rpcchainvm_proto_version
    )

    if module.params["strict"] and not result["is_compatible"]:
        module.fail_json(
            msg="VM and AvalancheGo versions are not compatible",
            **result,
        )

    # Exit with the result if there was no error
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
