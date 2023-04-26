# Changelog

## [v0.7.0](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.7.0) (2023-04-26)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.6.1...v0.7.0)

**Implemented enhancements:**

- Add Blockscout role [\#48](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/48)

**Merged pull requests:**

- feat: add blockscout role [\#49](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/49) ([leopaul36](https://github.com/leopaul36))

## [v0.6.1](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.6.1) (2023-03-30)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.6.0...v0.6.1)

**Breaking changes:**

- feat: remove ash node logic from node role [\#45](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/45) ([Nuttymoon](https://github.com/Nuttymoon))

**Implemented enhancements:**

- feat: add faucet role [\#42](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/42) ([leopaul36](https://github.com/leopaul36))

**Closed issues:**

- Remove Ash node logic from this collection [\#40](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/40)
- Avalanche Subnet faucet role [\#36](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/36)

**Merged pull requests:**

- docs: add changelog [\#43](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/43) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.6.0](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.6.0) (2023-03-23)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.5.1...v0.6.0)

**Breaking changes:**

- Rename `avalanche_tracked_subnets` variable to `avalanchego_track_subnets` [\#34](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/34)

**Implemented enhancements:**

- Verify AvalancheGo binary integrity before installation [\#37](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/37)
- Use Ava Labs releases of Subnet EVM [\#32](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/32)
- Try to use apt to install AvalancheGo [\#31](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/31)
- Support TLS for the HTTP API endpoints [\#26](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/26)

**Merged pull requests:**

- Add TLS support for HTTP API endpoints [\#41](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/41) ([Nuttymoon](https://github.com/Nuttymoon))
- AvalancheGo binary verification [\#38](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/38) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.5.1](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.5.1) (2023-03-20)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.5.0...v0.5.1)

**Breaking changes:**

- Use Ava Labs VM releases [\#33](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/33) ([Nuttymoon](https://github.com/Nuttymoon))

**Deprecated:**

- Drop support for blobvm, spacesvm and timestampvm [\#29](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/29)

## [v0.5.0](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.5.0) (2023-03-17)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.4.1...v0.5.0)

**Breaking changes:**

- feat: drop support for vms other than subnet-evm [\#30](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/30) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.4.1](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.4.1) (2023-03-14)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.4.0...v0.4.1)

**Closed issues:**

- Clean the plugins dir if avalanchego\_vms\_install is empty [\#27](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/27)
- Uniformize license headers [\#17](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/17)

**Merged pull requests:**

- fix: clean plugins dir if avalanchego\_vms\_install is empty [\#28](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/28) ([leopaul36](https://github.com/leopaul36))
- chore: uniformize license headers [\#24](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/24) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.4.0](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.4.0) (2023-02-27)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.3.1...v0.4.0)

**Implemented enhancements:**

- Adapt to the changes of v1.9.6 [\#18](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/18)
- Support subnet configs [\#8](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/8)

**Fixed bugs:**

- Bootstrapping a node without additional VMs currently fails [\#20](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/20)
- Adding validator to primary network should not be triggered if the validator is pending [\#6](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/6)

**Closed issues:**

- Bump VMs compatibility list [\#22](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/22)

**Merged pull requests:**

- fix: remove duplicate plugins dir creation [\#21](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/21) ([leopaul36](https://github.com/leopaul36))
- feat: adapt to 1.9.6 [\#19](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/19) ([leopaul36](https://github.com/leopaul36))
- fix: update subnetevm compatibility matrix [\#16](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/16) ([leopaul36](https://github.com/leopaul36))
- Ash node playbook [\#15](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/15) ([Nuttymoon](https://github.com/Nuttymoon))
- fix: check pending validators before addvalidator [\#14](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/14) ([Nuttymoon](https://github.com/Nuttymoon))
- feat: add subnets configs support [\#12](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/12) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.3.1](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.3.1) (2022-10-28)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.3.0...v0.3.1)

**Implemented enhancements:**

- Switch default network to fuji to avoid having to overwrite critical config in testnet/mainnet [\#3](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/3)

**Closed issues:**

- Document all playbooks [\#10](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/10)

**Merged pull requests:**

- feat: add convert ansible filter [\#13](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/13) ([Nuttymoon](https://github.com/Nuttymoon))
- docs: add playbooks desc to readme [\#11](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/11) ([Nuttymoon](https://github.com/Nuttymoon))
- feat: set fuji as default network [\#7](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/7) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.3.0](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.3.0) (2022-10-15)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.2.0...v0.3.0)

**Merged pull requests:**

- feat: update vms supported versions [\#5](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/5) ([Nuttymoon](https://github.com/Nuttymoon))
- docs: enable statistics for yaml [\#4](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/4) ([Nuttymoon](https://github.com/Nuttymoon))
- feat: add user and add validator tasks [\#2](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/2) ([leopaul36](https://github.com/leopaul36))

## [v0.2.0](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.2.0) (2022-07-21)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.1.6...v0.2.0)

**Merged pull requests:**

- Migrate collection to ash org [\#1](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/1) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.1.6](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.1.6) (2022-07-21)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.1.5...v0.1.6)

## [v0.1.5](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.1.5) (2022-06-22)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.1.4...v0.1.5)

## [v0.1.4](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.1.4) (2022-03-25)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.1.3...v0.1.4)

## [v0.1.3](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.1.3) (2022-03-25)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.1.2...v0.1.3)

## [v0.1.2](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.1.2) (2022-03-20)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.1.1...v0.1.2)

## [v0.1.1](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.1.1) (2022-03-17)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.1.0...v0.1.1)

## [v0.1.0](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.1.0) (2022-02-19)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/ace915f1b17eb1edf3a58a1471c506f210fba591...v0.1.0)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
