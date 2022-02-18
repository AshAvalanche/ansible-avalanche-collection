# Ansible Avalanche Collection

Collection providing Ansible roles, playbooks and modules to manage [Avalanche](https://docs.avax.network/) nodes, subnets and blockchains.

## Why an Ansible collection for Avalanche?

Ava Labs provides [avalanche-network-runner](https://github.com/ava-labs/avalanche-network-runner) to easily run a local test network (either locally or in Kubernetes).

This collection takes a different approach and provides tools for production environments. Those can also be used to bootstrap realistic test networks.

It aims at:

- **Provisioning Avalanche nodes** on Fuji or Mainnet with flawless upgrade capabilities. Ansible also brings easy node configuration persistence and idempotent deployments.
- **Bootstrapping local test networks** that really mimic production environments
- **Automating subnet and blockchain operations** (subnet whitelisting, plugin deployment) for validators
- And more

## Requirements

- Ansible >= 2.9 (see [Installing Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html))

## Supported versions

This collection has been tested to work with the following versions:

- Ubuntu 20.04
- AvalancheGo >= 1.7.0

## Installation

```sh
# With Ansible >= 2.10
ansible-galaxy collection install git+https://github.com/Nuttymoon/ansible-avalanche-collection.git

# With Ansible 2.9
mkdir -p ansible_collections/nuttymoon
git clone https://github.com/Nuttymoon/ansible-avalanche-collection.git ansible_collections/nuttymoon/avalanche
```

## Getting started

The repository [ansible-avalanche-getting-started](https://github.com/Nuttymoon/ansible-avalanche-getting-started) provides examples of how to use the collection.

## Collection resources

### Roles

- [nuttymoon.avalanche.node](./roles/node): install, configure and upgrade Avalanche nodes

### Playbooks

- [nuttymoon.avalanche.bootstrap_local_network](./playbooks/bootstrap_local_network.yml): bootstrap a local test network (`--network-id=local`)

## Inventory requirements

- **All the nodes** on which to install AvalancheGo have to be in the `avalanche_nodes` group.
- For local networks, **one of the nodes** has to be in the `bootstrap_node` group. This node has to **be started first to serve as a bootstrap node** for the others. For an example of how to do that, see the [bootstrap_local_network.yml](../../playbooks/bootstrap_local_network.yml) playbook.

## Roadmap

- [ ] Avalanche transactions module
- [ ] Subnet role
- [ ] Blockchain role
