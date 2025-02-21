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

### **Avalanche Nodes and Chains Configuration**

```yaml
erpc_endpoint_list:
  - "http://{{ hostvars['validator01'].ansible_host }}:9650"
  - "http://{{ hostvars['validator02'].ansible_host }}:9650"
  - "http://{{ hostvars['validator03'].ansible_host }}:9650"
  - "http://{{ hostvars['validator04'].ansible_host }}:9650"
  - "http://{{ hostvars['validator05'].ansible_host }}:9650"

erpc_chains:
  - name: C
    evm_id: 43113
    chain_id: C
```

### **Advanced Configuration**
These variable are taken into account using both playbooks.

```yaml
erpc_projects: [] # List of eRPC projects. The `erpc_chains` and `erpc_endpoint_list` variables will have no effect if this list is not empty.
erpc_aliasing_rules: [] # List of aliasing rules. By default, the first `erpc_chains` is accessible without a route.
erpc_limiters_budgets: [] # Management of request quotas.
```

## Usage

Run the following command if you need a simple configuration based on the network you deployed:
```sh
ansible-playbook ash.avalanche.install_erpc_network -i inventories/local
```

Run the following command if you need to customize used nodes and available chains:
```sh
ansible-playbook ash.avalanche.install_erpc_custom -i inventories/local
```

Pattern of available endpoint:
```
<erpc-ip>:4000/<evm-chain-id>
```
Example:
curl -X POST --data '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber","params":[]}' -H 'content-type:application/json;' $(terraform -chdir=terraform/multipass output -raw frontend_ip):4000/43113
