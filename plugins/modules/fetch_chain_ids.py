#!/usr/bin/python

# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2024, E36 Knots

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
import requests

__metaclass__ = type


def get_eth_chain_id(rpc_url):
    """Performs a JSON-RPC eth_chainId request."""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_chainId",
        "params": []
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(rpc_url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("result", None)
    except requests.exceptions.RequestException as e:
        return str(e)


def main():
    module_args = dict(
        rpc_url=dict(type="str", required=True),
        chains=dict(type="list", required=True),
        include_c_chain=dict(type="bool", required=False, default=True),
    )

    results = []

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    try:
        for chain in module.params["chains"]:
            fetched_chain_id = get_eth_chain_id(module.params["rpc_url"]+f"/ext/bc/{chain['chain_id']}/rpc")

            if fetched_chain_id is None:
                module.fail_json(msg="No response from the RPC.")

            results.append({'evm_id': int(fetched_chain_id, 16), **chain})

        if module.params["include_c_chain"]:
            results.append({'evm_id': 43113, 'chain_id': 'C', 'name': 'C'})

        module.exit_json(**{'results': results})

    except Exception:
        import traceback
        module.fail_json(msg=to_native(traceback.format_exc()))


if __name__ == "__main__":
    main()
