# Ansible Avalanche Collection

Collection providing Ansible roles, playbooks and modules to manage [Avalanche](https://docs.avax.network/) nodes, subnets and blockchains.

## Why an Ansible collection for Avalanche?

Ava Labs provides [avalanche-network-runner](https://github.com/ava-labs/avalanche-network-runner) to easily run a local test network (either locally or in Kubernetes).

This collection takes a different approach and provides tools for production environments. Those can also be used to bootstrap realistic test networks.

It aims at:

- **Provisioning Avalanche nodes** on Fuji or Mainnet with flawless upgrade capabilities. Ansible also brings easy node configuration persistence and idempotent deployments.
- **Bootstrapping local test networks** that really mimic production environments
- **Automating Subnet and blockchain operations** (subnet whitelisting, plugin deployment) for validators
- And more

## Requirements

- Ansible >= 2.9 (see [Installing Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html))

## Supported versions

This collection has been tested to work with the following versions:

- Ubuntu 20.04-22.04
- AvalancheGo >= 1.9.6

## Installation

```sh
ansible-galaxy collection install git+https://github.com/AshAvalanche/ansible-avalanche-collection.git
```

## Getting started

Follow the [tutorials](https://ash.center/docs/toolkit/ansible-avalanche-collection/tutorials/local-test-network) on the [Ash docs website](https://ash.center/) to get started!

## Documentation

Checkout [the reference documentation](https://ash.center/docs/toolkit/ansible-avalanche-collection/reference) on the [Ash docs website](https://ash.center/) for complete documentation.
