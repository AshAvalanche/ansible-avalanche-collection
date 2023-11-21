# Changelog

## [v0.9.0](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.9.0) (2023-11-21)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.10...v0.9.0)

**Closed issues:**

- Rename node staking TLS cert + key to a generic name [\#100](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/100)
- Select the VM arch based on the Ansible architecture value [\#98](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/98)

**Merged pull requests:**

- feat\(node\): create a parent directory in /var/lib [\#102](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/102) ([Nuttymoon](https://github.com/Nuttymoon))
- fix: VM binary arch [\#101](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/101) ([Nuttymoon](https://github.com/Nuttymoon))
- feat\(node\): support Docker image build [\#99](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/99) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.8.10](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.10) (2023-10-16)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.9...v0.8.10)

## [v0.8.9](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.9) (2023-10-10)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.8...v0.8.9)

**Closed issues:**

- Multipass simulates a Ubuntu ARM on a Mac M1  [\#96](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/96)

## [v0.8.8](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.8) (2023-08-31)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.7...v0.8.8)

**Implemented enhancements:**

- Add retries to the downloads tasks [\#90](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/90)
- Implement rolling restart mechanism [\#78](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/78)

**Fixed bugs:**

- The validation start/end times generation is broken on other OSs than Linux [\#92](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/92)

**Merged pull requests:**

- Nodes rolling restart [\#95](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/95) ([Nuttymoon](https://github.com/Nuttymoon))
- fix: register ansible's localhost for date command [\#94](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/94) ([leopaul36](https://github.com/leopaul36))

## [v0.8.7](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.7) (2023-08-28)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.6...v0.8.7)

**Breaking changes:**

- feat\(playbooks\): add add\_subnet\_validators [\#93](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/93) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.8.6](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.6) (2023-08-23)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.5...v0.8.6)

**Implemented enhancements:**

- The `ash_cmd` module should be in status `changed` if modifications were made [\#81](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/81)

**Security fixes:**

- Use an argument to pass the private key in `ash_cmd` module [\#79](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/79)

**Merged pull requests:**

- feat\(ash\_cmd\): improve mod security + output [\#91](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/91) ([Nuttymoon](https://github.com/Nuttymoon))

## [v0.8.5](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.5) (2023-08-07)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.4...v0.8.5)

**Breaking changes:**

- Chain aliases and public ip config [\#89](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/89) ([Nuttymoon](https://github.com/Nuttymoon))

**Implemented enhancements:**

- Allow to specify the validation parameters for each validator [\#87](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/87)
- Allow to configure the `public-ip` with a role variable instead of `ansible_host` [\#56](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/56)
- Use `chain-aliases-file` property to create chain aliases [\#39](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/39)

**Closed issues:**

- ash.avalanche.ash\_cli fails when ash\_cli\_custom\_networks = {} [\#85](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/85)

**Merged pull requests:**

- Subnet validators params [\#88](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/88) ([Nuttymoon](https://github.com/Nuttymoon))
- feat: verify ash\_cli\_custom\_networks is defined [\#86](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/86) ([leopaul36](https://github.com/leopaul36))

## [v0.8.4](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.4) (2023-07-26)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.3...v0.8.4)

## [v0.8.3](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.3) (2023-07-24)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.2...v0.8.3)

**Breaking changes:**

- Add Ansible tags + allow multiple bootstrap nodes [\#84](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/84) ([Nuttymoon](https://github.com/Nuttymoon))

**Implemented enhancements:**

- Allow to provide multiple bootstrap nodes [\#83](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/83)

**Closed issues:**

- Document the admin and validate features [\#9](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/9)

## [v0.8.2](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.2) (2023-07-06)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.1...v0.8.2)

**Breaking changes:**

- Fix add-validator vars propagation [\#82](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/82) ([Nuttymoon](https://github.com/Nuttymoon))

**Implemented enhancements:**

- Let users override computed avalanchego\_node\_json values [\#76](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/76)

**Fixed bugs:**

- Validator variables are not propagated properly in `avalanche.node.add-validator` [\#80](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/80)
- Validation period start/end time generation doesn't work on MacOS [\#73](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/73)

**Closed issues:**

- Implement v1.10.3 configurations changes [\#72](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/72)

**Merged pull requests:**

- feat: avalanchego\_node\_json precedence in combine [\#77](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/77) ([leopaul36](https://github.com/leopaul36))
- 73 date command per dist [\#75](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/75) ([leopaul36](https://github.com/leopaul36))
- feat: adapt config to v1.10.3 [\#74](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/74) ([leopaul36](https://github.com/leopaul36))

## [v0.8.1](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.1) (2023-06-14)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.8.0...v0.8.1)

**Merged pull requests:**

- feat\(ash\_cli\): unpack Ash CLI archive [\#71](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/71) ([Nuttymoon](https://github.com/Nuttymoon))
- feat: sync dashboards with avalanche-monitoring [\#70](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/70) ([leopaul36](https://github.com/leopaul36))

## [v0.8.0](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.8.0) (2023-06-09)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.7.6...v0.8.0)

**Breaking changes:**

- Use Ash CLI for API calls and transactions [\#69](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/69) ([Nuttymoon](https://github.com/Nuttymoon))

**Implemented enhancements:**

- Use Ash CLI to perform API calls and issue transactions [\#68](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/68)

## [v0.7.6](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.7.6) (2023-06-02)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.7.5...v0.7.6)

**Breaking changes:**

- 44 rename blockscout role [\#67](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/67) ([Nuttymoon](https://github.com/Nuttymoon))

**Closed issues:**

- Rename `avalanche_faucet_chains` to `avalanche_faucet_evmchains` [\#44](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/44)

## [v0.7.5](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.7.5) (2023-05-30)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.7.4...v0.7.5)

**Implemented enhancements:**

- Add Subnets dashboard to install\_monitoring\_stack [\#64](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/64)

**Merged pull requests:**

- feat: add subnets dashboard and logic [\#65](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/65) ([leopaul36](https://github.com/leopaul36))

## [v0.7.4](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.7.4) (2023-05-23)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.7.3...v0.7.4)

**Implemented enhancements:**

- Implement an Ash CLI module [\#62](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/62)

**Closed issues:**

- Deprecated roles' README [\#60](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/60)

**Merged pull requests:**

- feat: ash\_cli module [\#63](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/63) ([leopaul36](https://github.com/leopaul36))
- docs: link README to ash.center [\#61](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/61) ([leopaul36](https://github.com/leopaul36))

## [v0.7.3](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.7.3) (2023-05-15)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.7.2...v0.7.3)

**Implemented enhancements:**

- Certificate upload should be optional [\#58](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/58)

**Fixed bugs:**

- Missing variables for http-tls-\* [\#57](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/57)

**Merged pull requests:**

- fix: make http-tls certs upload optional [\#59](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/59) ([leopaul36](https://github.com/leopaul36))
- feat: bump avalanchego\_vms\_list [\#55](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/55) ([leopaul36](https://github.com/leopaul36))

## [v0.7.2](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.7.2) (2023-04-27)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.7.1...v0.7.2)

**Implemented enhancements:**

- Configure Ash CLI depending on the current network [\#53](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/53)
- Add a monitoring stack playbook [\#51](https://github.com/AshAvalanche/ansible-avalanche-collection/issues/51)

**Merged pull requests:**

- feat\(ash\_cli\): add config playbook [\#54](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/54) ([Nuttymoon](https://github.com/Nuttymoon))
- feat: monitoring stack [\#52](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/52) ([leopaul36](https://github.com/leopaul36))

## [v0.7.1](https://github.com/AshAvalanche/ansible-avalanche-collection/tree/v0.7.1) (2023-04-26)

[Full Changelog](https://github.com/AshAvalanche/ansible-avalanche-collection/compare/v0.7.0...v0.7.1)

**Implemented enhancements:**

- feat: add ash\_cli role [\#50](https://github.com/AshAvalanche/ansible-avalanche-collection/pull/50) ([Nuttymoon](https://github.com/Nuttymoon))

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
