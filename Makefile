.PHONY: all lint test format
SHELL:=/bin/bash

all: lint test

lint:
	flake8 .
	pydocstyle ../TelegramBots
	isort --check-only .
# 	black --check ../TelegramBots
	mypy .
	echo "done"