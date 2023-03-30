# ash.avalanche.node

This Ansible role allows to bootstrap Avalanche nodes:

- Install and configure [AvalancheGo](https://github.com/ava-labs/avalanchego) following Linux best practices
- Install Virtual Machines that can later be used to create blockchains
- (On local networks) Create an account with access to pre-funded addresses as described [here](https://docs.avax.network/build/tutorials/platform/fund-a-local-test-network)

## Role variables

| Variable                              | Comment                                                                                                                                                                                                                                                               | Default value                                                  |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `avalanchego_version`                 | See [AvalancheGo releases](https://github.com/ava-labs/avalanchego/releases)                                                                                                                                                                                          | `1.9.6`                                                        |
| `avalanchego_install_dir`             | Base directory to store all AvalancheGo software                                                                                                                                                                                                                      | `/opt/avalanche/avalanchego`                                   |
| `avalanchego_vms_dir`                 | Where to unpack VMs releases                                                                                                                                                                                                                                          | `/opt/avalanche/vms`                                           |
| `avalanchego_db_dir`                  | [--db-dir](https://docs.avax.network/build/references/avalanchego-config-flags#--db-dir-string-file-path) argument                                                                                                                                                    | `/var/lib/avalanchego/db`                                      |
| `avalanchego_conf_dir`                | Where to store AvalancheGo config files                                                                                                                                                                                                                               | `/etc/avalanche/avalanchego/conf`                              |
| `avalanchego_staking_certs_dir`       | Where to store the node's TLS certificates used to communicate with peers on the Avalanche network                                                                                                                                                                    | `/etc/avalanche/avalanchego/staking`                           |
| `avalanchego_https_certs_dir`         | Where to store the node's TLS certificates used to secure HTTP API endpoints                                                                                                                                                                                          | `/etc/ssl/certs/avalanche/avalanchego`                         |
| `avalanchego_log_dir`                 | Where to write logs                                                                                                                                                                                                                                                   | `/var/log/avalanche/avalanchego`                               |
| `avalanchego_user`                    | The user that will run the AvalancheGo Linux service                                                                                                                                                                                                                  | `avalanche`                                                    |
| `avalanchego_group`                   | The group of the user that will run the AvalancheGo Linux service                                                                                                                                                                                                     | `avalanche`                                                    |
| `avalanchego_http_host`               | [--http-host](https://docs.avax.network/build/references/avalanchego-config-flags#--http-host-string) argument                                                                                                                                                        | `127.0.0.1`                                                    |
| `avalanchego_http_port`               | [--http-port](https://docs.avax.network/build/references/avalanchego-config-flags#--http-port-int) argument                                                                                                                                                           | `9650`                                                         |
| `avalanchego_https_enabled`           | Whether to secure the HTTP API endpoints using TLS. See [--http-tls-enabled](https://docs.avax.network/nodes/maintain/avalanchego-config-flags#--http-tls-enabled-boolean) argument. If `true` will upload TLS certificates from `avalanchego_https_local_certs_dir`. | `false`                                                        |
| `avalanchego_https_local_certs_dir`   | Where to find the TLS certificates on the Ansible host                                                                                                                                                                                                                | `"{{ playbook_dir }}/files/https"`                             |
| `avalanchego_static_public_ip`        | Whether to statically set the node's [public IP](https://docs.avax.network/build/references/avalanchego-config-flags#public-ip). If `true` will use the IP provided in the inventory.                                                                                 | `true`                                                         |
| `avalanchego_staking_port`            | [--staking-port](https://docs.avax.network/build/references/avalanchego-config-flags#--staking-port-int) argument                                                                                                                                                     | `9651`                                                         |
| `avalanchego_staking_use_local_certs` | If `true` will upload TLS certificatesfrom `avalanchego_staking_local_certs_dir`. If `false` AvalancheGo will automatically create new certs.                                                                                                                         | `false`                                                        |
| `avalanchego_staking_local_certs_dir` | Where to find the existing certificateson the Ansible host                                                                                                                                                                                                            | `"{{ playbook_dir }}/files/staking"`                           |
| `avalanchego_network_id`              | See [Network ID](https://docs.avax.network/build/references/avalanchego-config-flags/#network-id)                                                                                                                                                                     | `fuji`                                                         |
| `avalanchego_bootstrap_node_id`       | The node ID of the bootstrap node                                                                                                                                                                                                                                     | `NodeID-7Xhw2mDxuDS44j42TCB6U5579esbSt3Lg`                     |
| `avalanchego_bootstrap_db`            | The local path to a snapshot of Avalanche database                                                                                                                                                                                                                    | `""`                                                           |
| `avalanchego_track_subnets`           | The list of tracked subnets that the node can validate. See [Subnet Tracking](https://docs.avax.network/nodes/maintain/avalanchego-config-flags#subnet-tracking)                                                                                                      | `[]`                                                           |
| `avalanchego_vms_install`             | The list of VMs to install on the node with their versions. VM names and versions are separated by `=`. See [VMs install](#vms-installation).                                                                                                                         | `[]`                                                           |
| `avalanchego_node_json`               | The AvalancheGo node configuration that will be dumped to `node.json` addresses                                                                                                                                                                                       | NA                                                             |
| `avalanchego_subnets_configs`         | The configuration of each subnet. See [Subnet Configs](https://docs.avax.network/nodes/maintain/subnet-configs) addresses                                                                                                                                             | `{}`                                                           |
| `avalanchego_chain_configs`           | The configuration of each chain. See [Chain Configs](https://docs.avax.network/nodes/maintain/chain-config-flags) addresses                                                                                                                                           | `{ C: { state-sync-enabled: true }}`                           |
| `avalanche_prefunded_username`        | The username to create and link to pre-funded addresses                                                                                                                                                                                                               | `ewoq`                                                         |
| `avalanche_prefunded_password`        | The password for `avalanche_prefunded_username`                                                                                                                                                                                                                       | `I_l1ve_@_Endor`                                               |
| `avalanche_prefunded_private_key`     | The private key used to access pre-funded addresses                                                                                                                                                                                                                   | `PrivateKey-ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN` |

**Note:** All config arguments are passed to AvalancheGo through a JSON config file stored at `avalanchego_config_dir`

## Inventory requirements

- **All the nodes** on which to install avalanchego have to be in the `avalanche_nodes` group.
- For local networks, **one of the nodes** has to be in the `bootstrap_node` group. This node has to **be started first to serve as bootstrap node** for the others. For an example of how to do that, see the [bootstrap_local_network.yml](../../playbooks/bootstrap_local_network.yml) playbook.

## Installation folders

The default installation follows [Linux Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html) by creating 3 main directories:

- `/opt/avalanche` to store **Avalanche softwares**
  - `└── avalanchego` contains the different versions of AvalancheGo
    - `└──current` contains symlinks to the currently used `avalanchego` binary and plugins
- `/etc/avalanche` to store **Avalanche related configuration files**
  - `├──  conf` contains AvalancheGo configs
  - `├── staking` contains the Avalanche node's TLS certificates
  - `└── gnupg` contains the AvalancheGo GPG keys used to sign the AvalancheGo binaries
- `/var/lib/avalanchego` to store **AvalancheGo data**
  - `└── db` contains AvalancheGo's database
- `/var/log/avalanche/avalanchego` to store **AvalancheGo logs**
- `/etc/ssl/certs/avalanche/avalanchego` to store **AvalancheGo TLS certificates** used to secure the node's HTTP API endpoints

**Note:** This differs from AvalancheGo default setup that stores the database and configuration files under `$HOME/.avalanchego`.

## VMs installation

To install a VM on the node, add it to `avalanchego_vms_install` following `VM_NAME=VM_VERSION` format (e.g. `timestampvm=1.2.0`).

**Note:** If `avalanchego_vms_install` is specified in your inventory, you have to list **all the VMs** to be installed (there isn't any merge with the default list).

### Available VMs and AvalancheGo compatibility

List of VMs currently available for installation:

- `subnet-evm`: The [Subnet EVM](https://github.com/ava-labs/subnet-evm) in versions `0.4.8` or later

Here is the compatibility matrix with AvalancheGo versions:

| AvalancheGo   | `subnet-evm`    |
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
