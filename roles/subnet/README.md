# ash.avalanche.subnet

This Ansible role allows to create an Avalanche subnet.

## Role variables

| Variable                        | Comment                                                                                                        | Default value                                           |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `avalanchego_http_host`         | [--http-host](https://docs.avax.network/build/references/avalanchego-config-flags#--http-host-string) argument | `127.0.0.1`                                             |
| `avalanchego_http_port`         | [--http-port](https://docs.avax.network/build/references/avalanchego-config-flags#--http-port-int) argument    | `9650`                                                  |
| `avalanchego_https_enabled`     | Wether the HTTP API endpoints are using TLS or not                                                             | `false`                                                 |
| `subnet_control_username`       | Username of the user that has control over the `subnet_control_keys`                                           | `ewoq`                                                  |
| `subnet_control_password`       | Password of the user that has control over the `subnet_control_keys`                                           | `I_l1ve_@_Endor`                                        |
| `subnet_control_keys_threshold` | The number of control keys needed to operate the Subnet                                                        | `2`                                                     |
| `subnet_control_keys`           | The list of control keys's addresses                                                                           | `[]`                                                    |
| `subnet_validators_weight`      | The weight to give to each validator of the Subnet                                                             | `1`                                                     |
| `subnet_validators_starttime`   | The time when validators start validating the Subnet                                                           | `'{{ lookup(''pipe'', ''date -d "5 minutes" +%s'') }}'` |
| `subnet_validators_endtime`     | The time when validators stop validating the Subnet                                                            | `'{{ lookup(''pipe'', ''date -d "1 month" +%s'') }}'`   |

## Inventory requirements

- **The node used to make API calls** have to be in the `subnet_control_node` group.
- **The nodes to be added as validators** to the Subnet have to be in the `subnet_validators` group. The Ansible host has to be able to connect to those nodes via SSH.

## How to?

See [ansible-avalanche-getting-started](https://github.com/AshAvalanche/ansible-avalanche-getting-started) for how to create a subnet.
