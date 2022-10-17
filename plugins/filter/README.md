# ash.avalanche filters

The collection provides the following filters:

- `ash.avalanche.convert`: convert an amount between AVAX units

## ash.avalanche.convert

### Usage

This filter is useful to submit transactions without errors in the number of zeros:

```yaml
ash.avalanche.tx:
  http_host: "{{ avalanchego_http_host }}"
  blockchain: X
  method: avm.send
  username: "{{ avax_transfer_from_username }}"
  password: "{{ avax_transfer_from_password }}"
  params:
    to: "{{ avax_transfer_to_address_bech32 }}"
    assetID: AVAX
    amount: "{{ 25 | ash.avalanche.convert('AVAX', 'nAVAX') | int }}"
```

### Supported units

| Unit              | Amount in wei                  |
| ----------------- | ------------------------------ |
| `wei`             | `1`                            |
| `gwei` or `navax` | `1e9` (`1000000000`)           |
| `avax` or `eth`   | `1e18` (`1000000000000000000`) |

**Note:** The filter is not case sensitive: `ash.avalanche.convert('AVAX', 'nAVAX')` is the same as `ash.avalanche.convert('avax', 'navax')`
