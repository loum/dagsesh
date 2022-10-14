.SILENT:
.DEFAULT_GOAL := help

include makester/makefiles/makester.mk
include makester/makefiles/docker.mk
include makester/makefiles/python-venv.mk
include makester/makefiles/versioning.mk

GITVERSION_VERSION := 5.10.1-alpine.3.14-6.0
GITVERSION_CONFIG := makester/sample/GitVersion.yml

# Add current Python virtual environment to path.
export PATH := 3env/bin:$(PATH)
export PYTHONPATH := src

# APP_ENV is used in setup.py.
ifndef APP_ENV
export APP_ENV := local
else
export APP_ENV := $(APP_ENV)
endif

init: WHEEL := .wheelhouse
init: clear-env makester-requirements
	$(info ### Installing "$(MAKESTER__PROJECT_NAME)" and dependencies ...)
	$(MAKE) pip-editable

TESTS := tests
tests:
	AIRFLOW__DAGSESH__PRIME_TEST_CONTEXT=true\
 $(PYTHON) -m pytest\
 --override-ini log_cli=true\
 --override-ini junit_family=xunit2\
 --log-cli-level=INFO -svv\
 --exitfirst\
 --cov-config tests/.coveragerc\
 --pythonwarnings ignore\
 --cov src\
 --junitxml tests/junit.xml\
 $(TESTS)

check-release-version:
	$(info ### Checking MAKESTER__VERSION)
	$(call check_defined, MAKESTER__VERSION)

package: WHEEL = .wheelhouse
package: APP_ENV = prod
package: check-release-version release-version

deps:
	pipdeptree

lint:
	-@pylint $(MAKESTER__PROJECT_DIR)/src

help: makester-help docker-help python-venv-help versioning-help
	@echo "(Makefile)\n\
  init                 Build the local Python-based virtual environment\n\
  deps                 Display PyPI package dependency tree\n\
  lint                 Lint the code base\n\
  tests                Run code test suite\n"

.PHONY: help tests
