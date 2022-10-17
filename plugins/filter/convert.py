#!/usr/bin/python
# Copyright 2022 TOSIT.IO
# SPDX-License-Identifier: Apache-2.0

from ansible.errors import AnsibleError


class FilterModule(object):
    def filters(self):
        return {'convert': self.convert}

    def convert(self, amount, from_unit, to_unit):
        units = {
            'wei': 1,
            'gwei': 1e9,
            'navax': 1e9,
            'avax': 1e18,
            'eth': 1e18,
        }

        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()

        if from_unit_lower not in units.keys() or to_unit_lower not in units.keys():
            raise AnsibleError(
                f'Unknown unit. Available units: {", ".join(units.keys())}'
            )

        return amount * units[from_unit_lower] / units[to_unit_lower]
