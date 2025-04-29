# Ansible Role: Graph Node for Avalanche

## Description

This Ansible role deploys and configures a **Graph Node** to index and query data from a single Avalanche blockchain. It integrates with IPFS and Postgres for efficient data management and exposes Prometheus-compatible metrics for monitoring.

## Features

- Automatic installation and configuration of Graph Node (with Docker).
- Integration with IPFS and Postgres.
- Customizable deployment for a user-specified blockchain.
- Exposes Prometheus-compatible metrics for monitoring.

## Prerequisites

- **Ansible** installed on your management machine.
- Access to Avalanche nodes and subnets.
- A running Postgres database and IPFS daemon.
- Prometheus server for monitoring (optional).

## Main Variables

Variables can be overridden in `defaults/main.yml` or via inventory files.

### **Basic Configuration**

```yaml
graph_node:
  version: latest
  user: root
  ports:
    graphql: 8000
    admin: 8020

  postgres:
    user: graph
    password: yqopFTn6n7MG0*FcG0*v
    db: graph
    port: 5432

  ipfs:
    port: 5001
    gateway_port: 8082

  RPC:
    network: subnet
    rpc_url: "http://<node-ip>:9650/ext/bc/<blockchain-id>/rpc"

  paths:
    conf: /etc/graph-node/conf
    custom: /etc/graph-node/conf/custom
    assets: /etc/graph-node/conf/custom/shared
    logs: /var/log/graph_node

  metrics:
    port: 8040 # Default port for Prometheus metrics
```

### **Advanced Configuration**

```yaml
graph_node_blockchain_id: "" # Specify the blockchain ID to deploy Graph Node for a specific blockchain.
```

## Usage

Run the following command to deploy Graph Node for a specific blockchain:
```sh
ansible-playbook ash.avalanche.install_graph_node -i inventories/local -e "graph_node_blockchain_id=<blockchain-id>"
```

## Prometheus Integration

Graph Node exposes Prometheus-compatible metrics on the following endpoint:
```
http://<frontend-ip>:8040/metrics
```

You can configure the metrics port using the `graph_node.metrics.port` variable.

Example Prometheus scrape configuration:
```yaml
scrape_configs:
  - job_name: 'graph-node'
    static_configs:
      - targets: ['<frontend-ip>:8040']
```

## Example Query

Once deployed, you can query the Graph Node using the GraphQL endpoint:
```sh
curl -X POST -H "Content-Type: application/json" \
  -d '{"query":"{ indexingStatuses { subgraph health } }"}' \
  http://<frontend-ip>:8000/subgraphs/name/<subgraph-name>
```
