# ash.avalanche.faucet

This Ansible role allows to deploy the [Avalanche Faucet](https://github.com/ava-labs/avalanche-faucet) as a Docker service.

| Variable                         | Comment                                                                                                              | Default value                     |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `avalanche_faucet_image`         | Base image of the Avalanche faucet                                                                                   | ghcr.io/ashavalanche/faucet-image |
| `avalanche_faucet_image_version` | Tag to be used                                                                                                       | disable-captcha-variable          |
| `avalanche_faucet_conf_dir`      | Where to store the faucet config files                                                                               | /etc/avalanche/faucet/conf        |
| `avalanche_faucet_log_dir`       | Where to store the faucet logs                                                                                       | /var/log/avalanche/faucet         |
| `avalanche_faucet_user`          | User that will run the faucet                                                                                        | faucet                            |
| `avalanche_faucet_group`         | Group of the user running the faucet                                                                                 | faucet                            |
| `avalanche_faucet_docker_group`  | Docker group of the target host                                                                                      | docker                            |
| `avalanche_faucet_port`          | Port on which the faucet will attach on the target host                                                              | 8000                              |
| `avalanche_faucet_chains`        | Config file for the faucet (see [docs](https://github.com/ava-labs/avalanche-faucet#setup-evm-chain-configurations)) | NA                                |
| `avalanche_faucet_env`           | Env file for the faucet (see [docs](https://github.com/ava-labs/avalanche-faucet#setup-environment-variables))       | NA                                |

## Inventory requirements

- The host on which to install the faucet have to be in the `faucet` group.

## How to?

See the [Subnet faucet](https://docs.ash.center/docs/tools/ansible-avalanche-collection/tutorials/subnet-faucet) tutorial to learn how to deploy the Avalanche Faucet.
