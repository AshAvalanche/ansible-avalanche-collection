#!/usr/bin/python
# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2023, E36 Knots

from ansible.errors import AnsibleError

import base58
from web3 import Web3


class FilterModule(object):
    def filters(self):
        return {
            'cb58_to_hex': self.cb58_to_hex,
            'cb58_to_bytes': self.cb58_to_bytes,
            'hex_to_cb58': self.hex_to_cb58,
            'hex_to_bytes': self.hex_to_bytes,
        }

    def cb58_to_hex(self, string):
        return base58.b58decode(string).hex()

    def cb58_to_bytes(self, string):
        return base58.b58decode(string)

    def hex_to_cb58(self, string):
        return base58.b58encode(bytearray.fromhex(string))

    def hex_to_bytes(self, string):
        return Web3.toBytes(hexstr=string)
