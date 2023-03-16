# ash.avalanche.node

This Ansible role allows to bootstrap Avalanche nodes:

- Install and configure [AvalancheGo](https://github.com/ava-labs/avalanchego) following Linux best practices
- Install Virtual Machines that can later be used to create blockchains
- (On local networks) Create an account with access to pre-funded addresses as described [here](https://docs.avax.network/build/tutorials/platform/fund-a-local-test-network)

## Role variables

| Variable                          | Comment                                                                                                                                                                                            | Default value                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `avalanchego_version`             | See [AvalancheGo releases](https://github.com/ava-labs/avalanchego/releases)                                                                                                                       | `1.9.0`                                                        |
| `avalanchego_install_dir`         | Base directory to store all AvalancheGo software                                                                                                                                                   | `/opt/avalanche/avalanchego`                                   |
| `avalanchego_vms_dir`             | Where to unpack VMs releases                                                                                                                                                                       | `/opt/avalanche/vms`                                           |
| `avalanchego_db_dir`              | [--db-dir](https://docs.avax.network/build/references/avalanchego-config-flags#--db-dir-string-file-path) argument                                                                                 | `/var/lib/avalanchego/db`                                      |
| `avalanchego_conf_dir`            | Where to store AvalancheGo config files                                                                                                                                                            | `/etc/avalanche/avalanchego/conf`                              |
| `avalanchego_certs_dir`           | Where to store the node's TLS certs                                                                                                                                                                | `/etc/avalanche/avalanchego/staking`                           |
| `avalanchego_log_dir`             | Where to write logs                                                                                                                                                                                | `/var/log/avalanche/avalanchego`                               |
| `avalanchego_user`                | The user that will run the AvalancheGo Linux service                                                                                                                                               | `avalanche`                                                    |
| `avalanchego_use_static_ip`       | Wether to explicitly set the node's [public IP](https://docs.avax.network/build/references/avalanchego-config-flags#public-ip). If `yes` will use the IP provided in the inventory.                | `yes`                                                          |
| `avalanchego_http_host`           | [--http-host](https://docs.avax.network/build/references/avalanchego-config-flags#--http-host-string) argument                                                                                     | `127.0.0.1`                                                    |
| `avalanchego_http_port`           | [--http-port](https://docs.avax.network/build/references/avalanchego-config-flags#--http-port-int) argument                                                                                        | `9650`                                                         |
| `avalanchego_staking_port`        | [--staking-port](https://docs.avax.network/build/references/avalanchego-config-flags#--staking-port-int) argument                                                                                  | `9651`                                                         |
| `avalanchego_log_level`           | [--log-level](https://docs.avax.network/build/references/avalanchego-config-flags/#--log-level-string-off-fatal-error-warn-info-debug-verbo) argument                                              | `info`                                                         |
| `avalanchego_network_id`          | See [Network ID](https://docs.avax.network/build/references/avalanchego-config-flags/#network-id)                                                                                                  | `fuji`                                                         |
| `avalanchego_use_existing_certs`  | If `yes` will upload TLS certs from `avalanchego_local_certs_dir`. If `no` AvalancheGo will automatically create new certs.                                                                        | `no`                                                           |
| `avalanchego_local_certs_dir`     | Where to find the existing certs on the Ansible host                                                                                                                                               | `"{{ playbook_dir }}/files/certs"`                             |
| `avalanchego_bootstrap_node_id`   | The node ID of the bootstrap node                                                                                                                                                                  | `NodeID-7Xhw2mDxuDS44j42TCB6U5579esbSt3Lg`                     |
| `avalanchego_bootstrap_db`        | The local path to a snapshot of Avalanche database                                                                                                                                                 | `""`                                                           |
| `avalanche_tracked_subnets`       | The list of tracked subnets that the node can validate. See [Subnet Tracking](https://docs.avax.network/nodes/maintain/avalanchego-config-flags#subnet-tracking) argument                          | `""`                                                           |
| `avalanchego_vms_install`         | The list of VMs to install on the node with their versions. VM names and versions are separated by `=`. See [VMs install](#vms-installation).                                                      | `['timestampvm=1.2.0']`                                        |
| `ash_node`                        | Wether the node is part of the Ash protocol. If `yes`, will enrich the node configuration with on-chain information. **Warning:** If the node is not known to the Ash protocol the role will fail. | `no`                                                           |
| `avalanchego_node_json`           | The AvalancheGo node configuration that will be dumped to `node.json` addresses                                                                                                                    | NA                                                             |
| `avalanchego_subnets_configs`     | The configuration of each subnet. See [Subnet Configs](https://docs.avax.network/nodes/maintain/subnet-configs) addresses                                                                          | `{}`                                                           |
| `avalanchego_chain_configs`       | The configuration of each chain. See [Chain Configs](https://docs.avax.network/nodes/maintain/chain-config-flags) addresses                                                                        | `{ C: { state-sync-enabled: true }}`                           |
| `avalanche_prefunded_username`    | The username to create and link to pre-funded addresses                                                                                                                                            | `ewoq`                                                         |
| `avalanche_prefunded_password`    | The password for `avalanche_prefunded_username`                                                                                                                                                    | `I_l1ve_@_Endor`                                               |
| `avalanche_prefunded_private_key` | The private key used to access pre-funded addresses                                                                                                                                                | `PrivateKey-ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN` |

**Note:** All config arguments are passed to AvalancheGo through a JSON config file stored at `avalanchego_config_dir`

## Inventory requirements

- **All the nodes** on which to install avalanchego have to be in the `avalanche_nodes` group.
- For local networks, **one of the nodes** has to be in the `bootstrap_node` group. This node has to **be started first to serve as bootstrap node** for the others. For an example of how to do that, see the [bootstrap_local_network.yml](../../playbooks/bootstrap_local_network.yml) playbook.

## Installation folders

The default installation follows [Linux Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html) by creating 3 main directories:

- `/opt/avalanche` to store **Avalanche softwares**
  - `/opt/avalanche/avalanchego` contains the different versions of AvalancheGo
    - `/opt/avalanche/avalanchego/current` contains symlinks to the currently used `avalanchego` binary and plugins
- `/etc/avalanche` to store **Avalanche related configuration files**
  - `/etc/avalanche/avalanchego/conf` contains AvalancheGo configs
  - `/etc/avalanche/avalanchego/staking` contains the Avalanche node's TLS certificates
- `/var/lib/avalanchego` to store **AvalancheGo data**
  - `/var/lib/avalanchego/db` contains AvalancheGo's database

**Note:** This differs from AvalancheGo default setup that stores the database and configuration files under `$HOME/.avalanchego`.

## VMs installation

To install a VM on the node, add it to `avalanchego_vms_install` following `VM_NAME=VM_VERSION` format (e.g. `timestampvm=1.2.0`).

**Note:** If `avalanchego_vms_install` is specified in your inventory, you have to list **all the VMs** to be installed (there isn't any merge with the default list).

### Available VMs and AvalancheGo compatibility

List of VMs currently available for installation:

- `subnetevm`: The [Subnet EVM](https://github.com/ava-labs/subnet-evm) in versions `0.4.8` or later

Here is the compatibility matrix with AvalancheGo versions:

| AvalancheGo   | `subnetevm`     |
| ------------- | --------------- |
| `1.9.6-1.9.8` | `0.4.8`         |
| `1.9.9`       | `0.4.9-0.4.10`  |
| `1.9.10`      | `0.4.11-0.4.12` |

**Note:** If a versions incompatibility is detected, an error message will be prompted and the role execution will stop.

## How to?

### Local test network

The [bootstrap_local_network.yml](../../playbooks/bootstrap_local_network.yml) playbook shows how to use this role to bootstrap a local test network.

See [ansible-avalanche-getting-started](https://github.com/AshAvalanche/ansible-avalanche-getting-started) for how to run the playbook and customize the installation.

### Fuji/Mainnet nodes

See [ansible-avalanche-getting-started](https://github.com/AshAvalanche/ansible-avalanche-getting-started) for how to provision Fuji/Mainnet nodes.
