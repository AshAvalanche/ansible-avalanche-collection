# ash.avalanche filters

The collection provides the following filters:

- [ash.avalanche.convert](#ashavalancheconvert): convert an amount between AVAX units
- [ash.avalanche.XXX_to_XXX](#ashavalanchexxx_to_xxx): convert a string between encodings

## ash.avalanche.convert

### Usage

This filter is useful to submit transactions without errors in the number of zeros:

```yaml
ash.avalanche.tx:
  ...
  params:
  	...
    amount: "{{ 25 | ash.avalanche.convert('AVAX', 'nAVAX') | int }}"
```

### Supported units

| Unit              | Amount in wei                  |
| ----------------- | ------------------------------ |
| `wei`             | `1`                            |
| `gwei` or `navax` | `1e9` (`1000000000`)           |
| `avax` or `eth`   | `1e18` (`1000000000000000000`) |

**Note:** The filter is not case sensitive: `ash.avalanche.convert('AVAX', 'nAVAX')` is the same as `ash.avalanche.convert('avax', 'navax')`

## ash.avalanche.XXX_to_XXX

### Usage

This is useful to convert string between different encodings, e.g. from hexadecimal to [CB58](https://support.avax.network/en/articles/4587395-what-is-cb58).

```yaml
# Example of cb58_to_hex conversion
- name: Convert NodeID to hexadecimal
  set_fact:
    node_id_hex: |-
      {{ (get_node_id_res.json.result.nodeID | split('-'))[1]
         | ash.avalanche.cb58_to_hex }}
```

### Supported conversions

- `cb58_to_hex`
- `cb58_to_bytes`
- `hex_to_cb58`
- `hex_to_bytes`
