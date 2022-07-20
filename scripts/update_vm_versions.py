#!/bin/python3

import os
import requests
import re
import yaml
from packaging import version

# Update the avalanchego_vms_list variable in roles/node/vars
# with new VM versions available and their compatibility with AvalancheGo

GITHUB_RAW_URL = 'https://raw.githubusercontent.com'
GITHUB_API_URL = 'https://api.github.com'

VARS_YAML_PATH = '../roles/node/vars/main.yml'
VARS_YAML_HEADER_SIZE = 3
VMS_REPOS = {
    'blobvm': 'AshAvalanche/blobvm',
    'spacesvm': 'AshAvalanche/spacesvm',
    'subnetevm': 'AshAvalanche/subnet-evm',
    # Versions not available in timestampvm's README
    # 'timestampvm': 'AshAvalanche/timestampvm',
}

vms_versions_comp = {}

# For each VM, fetch AvalancheGo compatibility info from README
for vm, repo in VMS_REPOS.items():
    repo_info = requests.get(f'{GITHUB_API_URL}/repos/{repo}')
    default_branch = repo_info.json()['default_branch']

    readme_url = f'{GITHUB_RAW_URL}/{repo}/{default_branch}/README.md'
    readme_raw = requests.get(readme_url)

    compatibility_specs = list(
        re.finditer(
            r'^\[v(?P<vm_start_ver>\d+\.\d+\.\d+)-?v?(?P<vm_end_ver>\d+\.\d+\.\d+)?\] '
            r'AvalancheGo@v(?P<avax_start_ver>\d+\.\d+\.\d+)-?v?(?P<avax_end_ver>\d+\.\d+\.\d+)?$',
            readme_raw.text,
            flags=re.MULTILINE,
        )
    )

    # Iterate on all versions
    versions_comp = {}
    for c in compatibility_specs:
        vm_start_ver = version.parse(c.group('vm_start_ver'))
        vm_end_ver = version.parse(c.group('vm_end_ver') or c.group('vm_start_ver'))

        for major in range(vm_start_ver.major, vm_end_ver.major + 1):
            for minor in range(vm_start_ver.minor, vm_end_ver.minor + 1):
                for micro in range(vm_start_ver.micro, vm_end_ver.micro + 1):
                    versions_comp.update(
                        {
                            f'{major}.{minor}.{micro}': {
                                'ge': c.group('avax_start_ver'),
                                'le': c.group('avax_end_ver')
                                or c.group('avax_start_ver'),
                            }
                        }
                    )

    vms_versions_comp.update({vm: versions_comp})

vars_yaml_abs_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), VARS_YAML_PATH
)

with open(vars_yaml_abs_path) as vars_yaml:
    vars_header = ''.join([vars_yaml.readline() for l in range(VARS_YAML_HEADER_SIZE)])
    vars_obj = yaml.load(vars_yaml, Loader=yaml.CLoader)

# Enrich the avalanchego_vms_list with updated versions_comp
for vm, v_comp in vms_versions_comp.items():
    vars_obj['avalanchego_vms_list'][vm]['versions_comp'] = v_comp

with open(vars_yaml_abs_path, 'w') as vars_yaml:
    vars_yaml.write(vars_header + yaml.dump(vars_obj, Dumper=yaml.CDumper))
