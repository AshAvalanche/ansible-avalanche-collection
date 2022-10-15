# ash.avalanche.node

This Ansible role allows to bootstrap Avalanche nodes:

- Install and configure [AvalancheGo](https://github.com/ava-labs/avalanchego) following Linux best practices
- Install Virtual Machines that can later be used to create blockchains
- (On local networks) Create an account with access to pre-funded addresses as described [here](https://docs.avax.network/build/tutorials/platform/fund-a-local-test-network)

## Role variables

| Variable                          | Comment                                                                                                                                                                             | Default value                                                  |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `avalanchego_version`             | See [AvalancheGo releases](https://github.com/ava-labs/avalanchego/releases)                                                                                                        | `1.9.0`                                                        |
| `avalanchego_binary_name`         | Don't change                                                                                                                                                                        | `"avalanchego-linux-amd64-v{{ avalanchego_version }}.tar.gz"`  |
| `avalanchego_binary_url`          | Don't change                                                                                                                                                                        | `"https://github.com/ava-labs/avalanchego/releases/download/`  |
|                                   |                                                                                                                                                                                     | `v{{ avalanchego_version }}/{{ avalanchego_binary_name }}"`    |
| `avalanchego_install_dir`         | Where to unpack AvalancheGo archive                                                                                                                                                 | `/opt/avalanche/avalanchego`                                   |
| `avalanchego_db_dir`              | [--db-dir](https://docs.avax.network/build/references/avalanchego-config-flags#--db-dir-string-file-path) argument                                                                  | `/var/lib/avalanchego/db`                                      |
| `avalanchego_conf_dir`            | Where to store AvalancheGo config files                                                                                                                                             | `/etc/avalanche/avalanchego/conf`                              |
| `avalanchego_certs_dir`           | Where to store the node's TLS certs                                                                                                                                                 | `/etc/avalanche/avalanchego/staking`                           |
| `avalanchego_log_dir`             | Where to write logs                                                                                                                                                                 | `/var/log/avalanche/avalanchego`                               |
| `avalanchego_vms_dir`             | Where to unpack VMs logs                                                                                                                                                            | `/opt/avalanche/vms`                                           |
| `avalanchego_user`                | The user that will run the AvalancheGo Linux service                                                                                                                                | `avalanche`                                                    |
| `avalanchego_use_static_ip`       | Wether to explicitly set the node's [public IP](https://docs.avax.network/build/references/avalanchego-config-flags#public-ip). If `yes` will use the IP provided in the inventory. | `yes`                                                          |
| `avalanchego_http_host`           | [--http-host](https://docs.avax.network/build/references/avalanchego-config-flags#--http-host-string) argument                                                                      | `127.0.0.1`                                                    |
| `avalanchego_http_port`           | [--http-port](https://docs.avax.network/build/references/avalanchego-config-flags#--http-port-int) argument                                                                         | `9650`                                                         |
| `avalanchego_staking_port`        | [--staking-port](https://docs.avax.network/build/references/avalanchego-config-flags#--staking-port-int) argument                                                                   | `9651`                                                         |
| `avalanchego_log_level`           | [--log-level](https://docs.avax.network/build/references/avalanchego-config-flags/#--log-level-string-off-fatal-error-warn-info-debug-verbo) argument                               | `info`                                                         |
| `avalanchego_network_id`          | See [Network ID](https://docs.avax.network/build/references/avalanchego-config-flags/#network-id)                                                                                   | `local`                                                        |
| `avalanchego_use_existing_certs`  | If `yes` will upload TLS certs from `avalanchego_local_certs_dir`. If `no` AvalancheGo will automatically create new certs.                                                         | `yes`                                                          |
| `avalanchego_local_certs_dir`     | Where to find the existing certs on the Ansible host                                                                                                                                | `"{{ playbook_dir }}/files/certs"`                             |
| `avalanchego_snow_sample_size`    | [--snow-sample-size-int](https://docs.avax.network/build/references/avalanchego-config-flags/#--snow-sample-size-int) argument                                                      | `2`                                                            |
| `avalanchego_snow_quorum_size`    | [--snow-quorum-size-int](https://docs.avax.network/build/references/avalanchego-config-flags/#--snow-quorum-size-int) argument                                                      | `2`                                                            |
| `avalanchego_bootstrap_node_id`   | The node ID of the bootstrap node                                                                                                                                                   | `NodeID-7Xhw2mDxuDS44j42TCB6U5579esbSt3Lg`                     |
| `avalanche_prefunded_username`    | The username to create and link to pre-funded addresses                                                                                                                             | `ewoq`                                                         |
| `avalanche_prefunded_password`    | The password for `avalanche_prefunded_username`                                                                                                                                     | `I_l1ve_@_Endor`                                               |
| `avalanche_prefunded_private_key` | The private key used to access pre-funded addresses                                                                                                                                 | `PrivateKey-ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN` |
| `avalanche_whitelisted_subnets`   | [--whitelisted-subnets-string](https://docs.avax.network/build/references/avalanchego-config-flags/#--whitelisted-subnets-string) argument                                          | `""`                                                           |
| `avalanchego_vms_install`         | The list of VMs to install on the node with their versions. VM names and versions are separated by `=`. See [VMs install](#vms-installation).                                       | `['timestampvm=1.2.0']`                                        |

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

List of VMs currently available for install:

- `blobvm`: The [Blob Virtual Machine](https://github.com/ava-labs/blobvm) in all versions
- `spacesvm`: The [Spaces Virtual Machine](https://github.com/ava-labs/spacesvm) in all versions
- `subnetevm`: The [Subnet EVM](https://github.com/ava-labs/subnet-evm) in all versions
- `timestampvm`: The [Timestamp Virtual Machine](https://github.com/ava-labs/timestampvm) in versions `1.2.0` and later

Here is the compatibility matrix with AvalancheGo versions:

| AvalancheGo     | `blobvm`      | `spacesvm`    | `subnetevm`   | `timestampvm` |
| --------------- | ------------- | ------------- | ------------- | ------------- |
| `1.7.0-1.7.4`   | -             | `0.0.1`       | `0.1.0`       | `1.2.0`       |
| `1.7.5-1.7.6`   | -             | `0.0.2`       | `0.1.1-0.1.2` | `1.2.2`       |
| `1.7.7-1.7.9`   | `0.0.1-0.0.2` | `0.0.3`       | `0.2.0`       | `1.2.3`       |
| `1.7.10`        | `0.0.3`       | `0.0.4`       | `0.2.1`       | `1.2.4`       |
| `1.7.11-1.7.12` | `0.0.4`       | `0.0.5`       | `0.2.2`       | `1.2.5`       |
| `1.7.13-1.7.18` | `0.0.5-0.0.7` | `0.0.6-0.0.7` | `0.2.3-0.2.5` | `1.2.6`       |
| `1.8.0-1.8.6`   | `0.0.8`       | `0.0.8`       | `0.3.0`       | -             |
| `1.9.0`         | `0.0.9`       | `0.0.9`       | `0.4.0`       | -             |

**Note:** If a versions incompatibility is detected, an error message will be prompted and the role execution will stop.

## How to?

### Local test network

The [bootstrap_local_network.yml](../../playbooks/bootstrap_local_network.yml) playbook shows how to use this role to bootstrap a local test network.

See [ansible-avalanche-getting-started](https://github.com/AshAvalanche/ansible-avalanche-getting-started) for how to run the playbook and customize the installation.

### Fuji/Mainnet nodes

See [ansible-avalanche-getting-started](https://github.com/AshAvalanche/ansible-avalanche-getting-started) for how to provision Fuji/Mainnet nodes.
