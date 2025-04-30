# Ansible Role: Graph Node for Avalanche

## Description

This Ansible role deploys and configures a **Graph Node** to index and query data from a single Avalanche blockchain. It integrates with IPFS and Postgres for efficient data management and exposes Prometheus-compatible metrics for monitoring.

## Features

- Automatic installation and configuration of Graph Node (via Docker).
- Integration with IPFS and Postgres.
- Customizable deployment for a user-specified Avalanche blockchain.
- Exposes Prometheus-compatible metrics for monitoring.

## Prerequisites

- **Ansible** installed on your management machine.
- Access to Avalanche nodes and subnets.
- A **running Postgres database** with specific locale and extensions (see below).
- An **IPFS daemon** available locally.
- (Optional) A Prometheus server for metrics scraping.

## Database Requirements

The PostgreSQL instance used by Graph Node must satisfy **strict requirements**.
Below are the **mandatory specs** for proper operation:

### Database Creation

```sql
CREATE DATABASE graph_test_db
  WITH OWNER = graph_test
       ENCODING = 'UTF8'
       LC_COLLATE = 'C'
       LC_CTYPE = 'C'
       TEMPLATE = template0;
```

### Required Extensions

Install the following **in the `graph_test_db` database**:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
CREATE EXTENSION IF NOT EXISTS postgres_fdw;
```

### User Permissions

The `graph_test` role must have **sufficient privileges**:

```sql
GRANT CREATE ON DATABASE graph_test_db TO graph_test;
GRANT USAGE ON SCHEMA public TO graph_test;
ALTER ROLE graph_test WITH SUPERUSER; -- Only if testing, not recommended in prod
```

> In production, it's best to create a role with granular rights for these extensions, instead of using `SUPERUSER`.

### pg_hba.conf Entry

Ensure your PostgreSQL server allows connections from the Graph Node host (e.g., Multipass VM):

```
host    graph_test_db    graph_test    10.172.69.109/32    md5
```

Then restart PostgreSQL:

```bash
sudo systemctl restart postgresql
```


## Main Variables

Override any of these in your inventory or with `-e` flags:

### **Basic Configuration**

```yaml
graph_node:
  version: v0.38.0
  user: root
  ports:
    graphql: 8000
    admin: 8020
  postgres:
    create: true
    user: graph
    password: yqopFTn6n7MG0*FcG0*v
    db: graph
    port: 5432
    graph_node_postgres_external:
      host: ""
      port: ""
      user: ""
      password: ""
      db: ""
  ipfs:
    host: ipfs
    port: 5001
    gateway_port: 8082
  RPC:
    network: subnet
    rpc_url: "http://127.0.0.1:9650/ext/bc/{{ graph_node_blockchain_id }}/rpc"
  paths:
    conf: /etc/graph-node
    custom: /etc/graph-node/conf/custom
    assets: /etc/graph-node/conf/custom/shared
    logs:   /var/log/graph_node
  metrics:
    port: 8040

graph_node_auto_restart: true
```

### **Advanced Configuration**

```yaml
graph_node_blockchain_id: "" # Blockchain ID to index
```

---

## Usage

Deploy Graph Node:

```bash
ansible-playbook ash.avalanche.install_graph_node.yml \
  -i inventories/local \
  -e "graph_node_blockchain_id=<blockchain-id>"
```

---

## Prometheus Integration

Graph Node exposes metrics here:
```
http://<frontend-ip>:8040/metrics
```

### Example Prometheus config:
```yaml
scrape_configs:
  - job_name: 'graph-node'
    static_configs:
      - targets: ['<frontend-ip>:8040']
```

---

## Example Query

Query GraphQL for indexing status:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query":"{ indexingStatuses { subgraph health } }"}' \
  http://<frontend-ip>:8000/subgraphs/name/<subgraph-name>
```

