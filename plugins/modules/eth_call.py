#!/usr/bin/python

# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2023, E36 Knots

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native

import re
from web3 import Web3
from hexbytes import HexBytes

__metaclass__ = type


# Cast bytes and int parameters to make sure they are in the right format
def cast_parameters(result):
    param_types = re.match(r'.+\((.+)\)', result['function_sig']).group(1).split(',')

    if len(param_types) != len(result['parameters']):
        result['msg'] = (
            'The number of parameters does not match function signature. '
            f'Expected {len(param_types)}, got {len(result["parameters"])}'
        )
        result['failed'] = True
        return

    casted_params = []

    for i, p in enumerate(result['parameters']):
        if 'bytes' in param_types[i]:
            casted_params.append(HexBytes(p))
        elif 'int' in param_types[i]:
            casted_params.append(int(p))
        else:
            casted_params.append(p)

    result['casted_params'] = casted_params


def eth_call(result):
    c_chain = Web3(Web3.HTTPProvider(result['rpc_url']))

    ash_router = c_chain.eth.contract(
        address=result['contract_addr'], abi=result['abi']
    )

    result['call_return'] = ash_router.get_function_by_signature(
        result['function_sig']
    )(*result['casted_params']).call()


def main():
    module_args = dict(
        rpc_url=dict(type='str', required=True),
        contract_addr=dict(type='str', required=True),
        abi=dict(type='raw', required=True),
        function_sig=dict(type='str', required=True),
        parameters=dict(type='raw', required=True),
    )

    result = {'changed': False, 'failed': False}

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    result['rpc_url'] = module.params['rpc_url']
    result['contract_addr'] = module.params['contract_addr']
    result['abi'] = module.params['abi']
    result['function_sig'] = module.params['function_sig']
    result['parameters'] = module.params['parameters']

    try:
        cast_parameters(result)
        if result['failed']:
            module.exit_json(**result)

        eth_call(result)
        result.pop('casted_params')

        module.exit_json(**result)

    except Exception:
        import traceback

        module.fail_json(msg=to_native(traceback.format_exc()))


if __name__ == '__main__':
    main()
