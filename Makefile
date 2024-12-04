SHELL := /bin/bash
.DEFAULT_GOAL := help

run_tests: ## Run unittests
	python3 -m unittest Tests/*.py
	cat Output/*

run_latest: ## Run latest day
	python3 -m unittest $(shell ls Tests/Day*.py -Art | tail -n 1)
	cat Output/*

help: ## Shows this help page
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
