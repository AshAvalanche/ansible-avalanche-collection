# ash.avalanche.blockchain

This Ansible role allows to create an Avalanche blockchain.

## Role variables

| Variable                    | Comment                                                                                                                                                                                                                               | Default value                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `avalanchego_http_host`     | [--http-host](https://docs.avax.network/build/references/avalanchego-config-flags#--http-host-string) argument                                                                                                                        | `127.0.0.1`                                         |
| `avalanchego_http_port`     | [--http-port](https://docs.avax.network/build/references/avalanchego-config-flags#--http-port-int) argument                                                                                                                           | `9650`                                              |
| `subnet_id`                 |                                                                                                                                                                                                                                       | `aUC7SX8QGVwsbwS4YNuavVTbinjJLrPjNNjdpZbbcFZZFSxFd` |
| `subnet_control_username`   |                                                                                                                                                                                                                                       | `ewoq`                                              |
| `subnet_control_password`   |                                                                                                                                                                                                                                       | `I_l1ve_@_Endor`                                    |
| `blockchain_vm`             | The VM used by the blockchain. See [Available VMs and AvalancheGo compatibility](../node/README.md#available-vms-and-avalanchego-compatibility) for the names to use.                                                                 | `timestampvm`                                       |
| `blockchain_name`           | The blockchain name.                                                                                                                                                                                                                  | `Timestamp Chain`                                   |
| `blockchain_aliases`        | The aliases to be linked to this blockchain. See [VM Configs](https://docs.avax.network/build/references/avalanchego-config-flags#vm-configs).                                                                                        | `['timestamp']`                                     |
| `blockchain_genesis_params` | The params passed to the gensis function of the VM to build the blockchain genesis state. See [Create the Genesis Data](https://docs.avax.network/build/tutorials/platform/subnets/create-custom-blockchain#create-the-genesis-data). | `{'data': 'Hello world'}`                           |

## Inventory requirements

- **The node used to make API calls** have to be in the `subnet_control_node` group.
- **The subnet validators** have to be in the `subnet_validators` group. The Ansible host has to be able to connect to those nodes via SSH (to create blockchain aliases.

## How to?

See [ansible-avalanche-getting-started](https://github.com/AshAvalanche/ansible-avalanche-getting-started) for how to create a blockchain.
