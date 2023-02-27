#!/usr/bin/python

# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2023, E36 Knots

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import jsonify
from ansible.module_utils._text import to_native
from ansible.module_utils.urls import Request

import json
import time

__metaclass__ = type


BLOCKCHAINS_TX_STATUS = {
    'P': {
        'method': 'platform.getTxStatus',
        'status': ['Committed', 'Dropped', 'Processing', 'Unknown'],
    },
    'X': {
        'method': 'avm.getTxStatus',
        'status': ['Accepted', 'Rejected', 'Processing', 'Unknown'],
    },
    'C/avax': {
        'method': 'avax.getAtomicTxStatus',
        'status': ['Accepted', 'Dropped', 'Processing', 'Unknown'],
    },
}


def call_avalanche_api(endpoint, data):
    r = Request()
    return json.loads(
        r.open(
            'POST', endpoint, headers={'Content-Type': 'application/json'}, data=data
        ).read()
    )


def submit_tx(result, retry_if_unknown, max_retries, num_retries=0):
    submit_resp = call_avalanche_api(result['endpoint'], jsonify(result['tx_data']))

    if submit_resp.get('error', False):
        result['failed'] = True
        result['msg'] = (
            'The API call returned an error. ' 'See response.result.error for details.'
        )
        return submit_resp
    elif not submit_resp['result'].get('txID', False):
        result['failed'] = True
        result['msg'] = (
            f'The method called ({result["tx_data"]["method"]}) '
            'does not create a transaction.'
        )
        return submit_resp

    # Get tx status
    result['tx_id'] = submit_resp['result']['txID']
    tx_status_data = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': BLOCKCHAINS_TX_STATUS[result['blockchain']]['method'],
        'params': {'txID': result['tx_id']},
    }
    status_resp = call_avalanche_api(result['endpoint'], jsonify(tx_status_data))

    unknown_status = BLOCKCHAINS_TX_STATUS[result['blockchain']]['status'][3]

    # Retry to submit tx if it's unknown by the node
    if status_resp['result']['status'] == unknown_status and retry_if_unknown:
        if num_retries == max_retries:
            result['failed'] = True
            return status_resp
        else:
            return submit_tx(result, retry_if_unknown, num_retries + 1)

    result['changed'] = True
    result['num_retries'] = num_retries
    return status_resp


def wait_tx_validation(result, timeout):
    tx_status = result['response']['result']['status']
    accepted_status, rejected_status = BLOCKCHAINS_TX_STATUS[result['blockchain']][
        'status'
    ][0:2]
    tx_status_data = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': BLOCKCHAINS_TX_STATUS[result['blockchain']]['method'],
        'params': {'txID': result['tx_id']},
    }

    start_time = time.time()
    elapsed_time = time.time() - start_time

    while tx_status not in [accepted_status, rejected_status]:
        time.sleep(5)
        status_resp = call_avalanche_api(result['endpoint'], jsonify(tx_status_data))
        tx_status = status_resp['result']['status']

        if elapsed_time >= timeout:
            result['failed'] = True
            result['msg'] = 'Timeout reached while waiting for transaction validation.'
            return status_resp

        elapsed_time = time.time() - start_time

    if tx_status == rejected_status:
        result['failed'] = True
        result['msg'] = 'The transaction was rejected by the network.'
        return status_resp

    return status_resp


def main():
    module_args = dict(
        blockchain=dict(type='str', required=True, aliases=['chain']),
        method=dict(type='str', required=True),
        username=dict(type='str', required=True, no_log=True),
        password=dict(type='str', required=True, no_log=True),
        params=dict(type='raw', required=True),
        http_host=dict(type='str', default='127.0.0.1'),
        http_port=dict(type='str', default='9650'),
        protocol=dict(type='str', default='http', choices=['http', 'https']),
        retry_if_unknown=dict(type='bool', default=True),
        max_retries=dict(type='int', default=5),
        wait_validation=dict(type='bool', default=False),
        wait_timeout=dict(type='int', default=300),
    )

    result = {'changed': False, 'failed': False}

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    blockchain = module.params['blockchain']
    method = module.params['method']
    username = module.params['username']
    password = module.params['password']
    params = module.params['params']
    host = module.params['http_host']
    port = module.params['http_port']
    protocol = module.params['protocol']
    retry_if_unknown = module.params['retry_if_unknown']
    max_retries = module.params['max_retries']
    wait_validation = module.params['wait_validation']
    wait_timeout = module.params['wait_timeout']

    try:
        result['blockchain'] = blockchain
        result['endpoint'] = f'{protocol}://{host}:{port}/ext/bc/{blockchain}'
        params.update({'username': username, 'password': password})
        result['tx_data'] = {
            'jsonrpc': '2.0',
            'id': 1,
            'method': method,
            'params': params,
        }

        if result['blockchain'] not in BLOCKCHAINS_TX_STATUS.keys():
            result[
                'msg'
            ] = f'The blockchain "{result["blockchain"]}" is not supported by this module.'
            result['failed'] = True
            module.exit_json(**result)

        if module.check_mode:
            module.exit_json(**result)

        result['response'] = submit_tx(result, retry_if_unknown, max_retries)

        if result['failed']:
            module.exit_json(**result)

        if wait_validation:
            result['response'] = wait_tx_validation(result, wait_timeout)

            if result['failed']:
                module.exit_json(**result)

        module.exit_json(**result)

    except Exception:
        import traceback

        module.fail_json(msg=to_native(traceback.format_exc()))


if __name__ == '__main__':
    main()
