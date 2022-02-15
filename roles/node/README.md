# nuttymoon.avalanche.node

This Ansible role allows to bootstrap Avalanche nodes. It installs and configures [avalanchego](https://github.com/ava-labs/avalanchego).

## Installation folders

The default installation follows [Linux Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html) by creating 3 main directories:

- `/opt/avalanche` to store Avalanche softwares
  - `/opt/avalanche/avalanchego` contains the different versions of avalanchego
    - `/opt/avalanche/avalanchego/current` contains symlinks to the currently used `avalanchego` binary and plugins
- `/etc/avalanche` to store Avalanche related configuration files
  - `/etc/avalanche/avalanchego/conf` contains avalanchego configs
  - `/etc/avalanche/avalanchego/staking` contains the Avalanche node's TLS certificates
- `/var/lib/avalanchego` to store avalanchego data
  - `/var/lib/avalanchego/db` contains avalanchego's database

**Note:** This differs from avalanchego defaults that store the database and configuration files under `$HOME/.avalanchego`.
