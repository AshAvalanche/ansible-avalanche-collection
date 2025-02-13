#!/usr/bin/python
# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022-2024, E36 Knots

from ansible.errors import AnsibleError

class FilterModule(object):
    def filters(self):
        return {"subnets_to_blockchains": self.subnets_to_blockchains}
    
    def find(self, dict_list: list, key: str, value: str, pop: bool = False):
        for index, item in enumerate(dict_list):
            if item[key] == value:
                if pop:
                    return dict_list.pop(index)
                return item
    
    def subnets_to_blockchains(self, subnet_list: list):
        primary_network = self.find(subnet_list, 'id', '11111111111111111111111111111111LpoYY', True)

        if not primary_network:
            raise AnsibleError("Primary network not found in subnet list")
        
        ids = []
        for subnet in subnet_list:
            if len(subnet["blockchains"]):
                for bc in subnet["blockchains"]:
                    ids.append({'name': bc['name'], 'chain_id': bc['id']})

        return ids
