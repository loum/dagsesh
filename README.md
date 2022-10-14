
# Dagsesh: Airflow DAG Session Manager

- [Overview](#Overview)
- [Prequisites](#Prerequisites)
  - [Upgrading GNU Make (macOS)](#Upgrading-GNU-Make-(macOS))
- [Getting Started](#Getting-Started)
  - [Creating the Local Environment](#Creating-the-Local-Environment)
    - [Local Environment Maintenance](#Local-Environment-Maintenance)
- [Using `dagsesh` Plugin in your Project's Test Suite](#Using-dagsesh-Plugin-in-your-Project's-Test-Suite)
- [FAQs](#FAQs)

## Overview
An Apache Airflow session context manager that overrides the default `AIRFLOW_HOME` path with a random, ephemeral alternate.

Why is this useful? As per the [Airflow configuration docs](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html):

> The first time you run Airflow, it will create a file called `airflow.cfg` in your `$AIRFLOW_HOME` directory (`~/airflow` by default).

Dagsesh delays the creation of `AIRFLOW_HOME` using a lazy-loading facility whilst injecting it with a random alternate. Great if you want to create a pristine Airflow environment for repeatable testing.

Dagsesh can be used as a convenient [pytest](https://docs.pytest.org/en/latest/contents.html) plugin to prime an Airflow environment for testing.

## Prerequisties
- [GNU make](https://www.gnu.org/software/make/manual/make.html)
- Python 3.10 Interpreter [(we recommend installing pyenv)](https://github.com/pyenv/pyenv)
- [Docker](https://www.docker.com/)

### Upgrading GNU Make (macOS)
Although the macOS machines provide a working GNU `make` it is too old to support the capabilities within the DevOps utilities packag
e, [makester](https://github.com/loum/makester). Instead, it is recommended to upgrade to the GNU `make` version provided by Homebrew
. Detailed instructions can be found at https://formulae.brew.sh/formula/make . In short, to upgrade GNU make run:
```
brew install make
```
The `make` utility installed by Homebrew can be accessed by `gmake`. The https://formulae.brew.sh/formula/make notes suggest how you
can update your local `PATH` to use `gmake` as `make`. Alternatively, alias `make`:
```
alias make=gmake
```
## Getting Started
### Building the Local Environment
Get the code and change into the top level `git` project directory:
```
git clone https://github.com/loum/dagsesh.git && cd dagsesh
```
> **_NOTE:_** Run all commands from the top-level directory of the `git` repository.

For first-time setup, prime the [Makester project](https://github.com/loum/makester.git):
```
git submodule update --init
```
Initialise the environment:
```
make pristine
```
#### Local Environment Maintenance
Keep [Makester project](https://github.com/loum/makester.git) up-to-date with:
```
git submodule update --remote --merge
```
### Help
There should be a `make` target to get most things done. Check the help for more information:
```
make help
```
### Running the Test Harness
Tests are good. We use [pytest](https://docs.pytest.org/en/latest/). To run the tests:
```
make tests
```
## Using `dagsesh` Plugin in your Project's Test Suite
Add the `dagsesh` package as a dependency to your project's development environment so that the
plugin is installed and visible in your `PYTHONPATH`.  `dagsesh` takes care of the distribution's
entry point so that `pytest` automatically finds the plugin module.  Nothing else needs to be done.

> **_NOTE:_** See [Making your plugin installable by others](https://docs.pytest.org/en/latest/how-to/writing_plugins.html#making-your-plugin-installable-by-others) for more information.

## FAQs
**_Q. Why is the default make on macOS so old?_**
Apple seems to have an issue with licensing around GNU products: more specifically to the terms of the GPLv3 license agreement. It is unlikely that Apple will provide current versions of utilities that are bound by the GPLv3 licensing constraints.

---
[top](#Dagsesh-Airflow-DAG-Session-Manager)
