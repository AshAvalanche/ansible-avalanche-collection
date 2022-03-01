# nuttymoon.avalanche modules

The collection provides the following modules:

- `nuttymoon.avalanche.tx` (alias: `nuttymoon.avalanche.transaction`): submit a transaction to an Avalanche network

## nuttymoon.avalanche.tx

### Supported API methods

- [Platform Chain (P-Chain) API](https://docs.avax.network/build/avalanchego-apis/p-chain): all the methods that create a transaction
- [Exchange Chain (X-Chain) API](https://docs.avax.network/build/avalanchego-apis/x-chain): all the methods that create a transaction
- [Contract Chain (C-Chain) API](https://docs.avax.network/build/avalanchego-apis/c-chain): only **Avalanche specific methods** (see [Avalanche Specific APIs](https://docs.avax.network/build/avalanchego-apis/c-chain/#avalanche-specific-apis)) that create a transaction

**Note:** You can identify transaction methods by looking at its signature: **it returns a `txID`**. E.g. for the `avm.import` method of the X-Chain:

```cpp
avm.import({
    to: string,
    sourceChain: string,
    username: string,
    password: string,
}) -> {
	txID: string // This tells us that avm.import() creates a transaction
}
```

### Module arguments

| Argument                | Required | Type   | Default value | Comment                                                                                                  |
| ----------------------- | -------- | ------ | ------------- | -------------------------------------------------------------------------------------------------------- |
| `blockchain` or `chain` | Yes      | `str`  | `None`        | Blockchain to query. Can be `P`, `X` or `C/avax`                                                         |
| `method`                | Yes      | `str`  | `None`        | API method to call                                                                                       |
| `username`              | Yes      | `str`  | `None`        | Username of the user that will pay the transaction fees (and owns addresses in case of send transaction) |
| `password`              | Yes      | `str`  | `None`        | Password of the user. It is recommended to store the password in an Ansible vault.                       |
| `params`                | Yes      | `raw`  | `None`        | Parameters of the method (except `username` and `password`)                                              |
| `http_host`             | No       | `str`  | `'127.0.0.1'` | IP address that exposes the JSON RPC API                                                                 |
| `http_port`             | No       | `str`  | `9650`        | Port that exposes the JSON RPC API                                                                       |
| `protocol`              | No       | `str`  | `'http'`      | `http` or `https`                                                                                        |
| `retry_if_unknown`      | No       | `bool` | `True`        | Retry to submit the transaction in case the transaction's status is `Unknown`                            |
| `max_retries`           | No       | `int`  | `5`           | Maximum number of retries in case the transaction's status is `Unknown`                                  |
| `wait_validation`       | No       | `bool` | `False`       | Wait for the transaction to be validated by the network                                                  |
| `wait_timeout`          | No       | `int`  | `300`         | Timeout when waiting for the transaction's validation                                                    |

**Note:** `username` and `password` are not redacted in the module output (replaced by `VALUE_SPECIFIED_IN_NO_LOG_PARAMETER`).

### JSON RPC endpoint construction

The JSON RPC endpoint used for the API calls is constructed as follows:

```jinja
{{ protocol }}://{{ http_host }}:{{ http_port }}/ext/bc/{{ blockchain }}
```

Some blockchains, like the C-Chain, have multiple RPC endpoints (see [Contract Chain (C-Chain) API](https://docs.avax.network/build/avalanchego-apis/c-chain/)). You have to specify the desired endpoint to use with the `blockchain` argument, e.g.:

```yaml
blockchain: C/avax
```

### Example playbook

The playbook [nuttymoon.avalanche.transfer_avax](../../playbooks/transfer_avax.yml) is provided as an example of how to use the `nuttymoon.avalanche.tx` module. See [ansible-avalanche-getting-started](https://github.com/Nuttymoon/ansible-avalanche-getting-started) for more.
