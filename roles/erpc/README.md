# Ansible Role: eRPC for AvalancheGo

## Description

This Ansible role allows deploying and configuring an **eRPC** server to interact with **AvalancheGo** nodes. It optimizes request management by preventing bottlenecks.

## Features

- Automatic installation and configuration of eRPC (with Docker and Systemd)
- Default support for the Avalanche C-Chain.
- Dynamic management of aliasing rules and upstreams.
- Configuration of rate limiters for traffic control.

## Prerequisites

- **Ansible** installed on your management machine.
- Access to **AvalancheGo** nodes.

## Main Variables

Variables can be overridden in `default/main.yml` or via inventory files.

### **Basic Configuration**

```yaml
erpc_version: 0.0.35

erpc_auto_restart: true

erpc_user: root

erpc_conf_dir: /etc/erpc/conf
erpc_custom_dir: "{{ erpc_conf_dir }}/custom"
```

### **Avalanche Nodes**

```yaml
erpc_endpoint_list:
  - "http://localhost:8545"

erpc_chains:
  - name: C
    evm_id: 43113
    chain_id: C
```

### **Advanced Configuration**

```yaml
erpc_projects: [] # List of eRPC projects. The `erpc_chains` and `erpc_endpoint_list` variables will have no effect if this list is not empty.
erpc_aliasing_rules: [] # List of aliasing rules. By default, the first `erpc_chains` is accessible without a route.
erpc_limiters_budgets: [] # Management of request quotas.
```

## Usage

Run the following command:

```sh
ansible-playbook ash.avalanche.install_erpc_docker -i inventories/local
```
