[![CircleCI](https://circleci.com/gh/GSA/datagov-deploy-dashboard.svg?style=svg)](https://circleci.com/gh/GSA/datagov-deploy-dashboard)


# datagov-deploy-dashboard

Ansible role to deploy the [Project Open Data
Dashboard](https://labs.data.gov/dashboard) on the Data.gov platform. This is
part of [GSA/datagov-deploy](https://github.com/GSA/datagov-deploy).


## Usage

This role assumes you've already installed git, nginx, php, php-fpm, and
composer. Add this role and its dependencies to your requirements.yml file.

```yaml
---
- src: https://github.com/GSA/datagov-deploy-dashboard
  version: v1.0.0
  name: gsa.datagov-deploy-dashboard
- src: geerlingguy.composer
- src: geerlingguy.git
- src: geerlingguy.php
- src: geerlingguy.php-versions
- src: nginxinc.nginx
```

Install with ansible-galaxy.

    $ ansible-galaxy install -r requirements.yml

Example playbook.

```yaml
---
- name: install dashboard
  roles:
    - role: geerlingguy.git
    - role: geerlingguy.php-versions
    - role: geerlingguy.php
    - role: geerlingguy.composer
    - role: nginxinc.nginx
    - role: gsa.datagov-deploy-dashboard
```


### Variables


#### `dashboard_php_major_minor_version` default: "7.3"

The major-minor version of PHP to install against.


## Development

### Prerequisites

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/) 3.6+
- [pipenv](https://docs.pipenv.org/en/latest/)


### Setup

Install dependencies.

    $ pipenv install --dev

Run the tests.

    $ pipenv run molecule test --all

For more information on how to use
[Molecule](https://molecule.readthedocs.io/en/latest/) for development, see [our
wiki](https://github.com/GSA/datagov-deploy/wiki/Developing-Ansible-roles-with-Molecule).


## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.


## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in
[CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright
> and related rights in the work worldwide are waived through the [CC0 1.0
> Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication.
> By submitting a pull request, you are agreeing to comply with this waiver of
> copyright interest.
