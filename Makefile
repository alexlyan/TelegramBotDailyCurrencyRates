export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ;               # no need for @

setup: ## Setup Virtual Env
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements/dev.txt

deps: ## Install dependencies
	./venv/bin/pip3 install -r requirements/dev.txt

lint: ## Runs black for code formatting
	./venv/bin/black . --exclude venv

clean: ## Clean package
	find . -type d -name '__pycache__' | xargs rm -rf
	rm -rf build dist

deploy: clean ## Copies any changed file to the server
	ssh ${PROJECTNAME} -C 'bash -l -c "mkdir -vp ./${PROJECTNAME}"'
	rsync -avzr \
		env.cfg \
		main.py \
		bot \
		common \
		request_rate \
		config \
		requirements \
		scripts \
		${PROJECTNAME}:./${PROJECTNAME}

start: deploy ## Sets up a screen session on the server and start the app
	ssh ${PROJECTNAME} -C 'bash -l -c "./${PROJECTNAME}/scripts/setup_bot.sh ${PROJECTNAME}"'

stop: deploy ## Stop any running screen session on the server
	ssh ${PROJECTNAME} -C 'bash -l -c "./${PROJECTNAME}/scripts/stop_bot.sh ${PROJECTNAME}"'

server: deploy ## Sets up dependencies required to run this bot
	ssh ${PROJECTNAME} -C 'bash -l -c "./${PROJECTNAME}/scripts/setup_dependencies.sh"'

ssh: ## SSH into the target VM
	ssh ${PROJECTNAME}

run: lint ## Run bot locally
	./venv/bin/python3 main.py

.PHONY: all lint test format
SHELL:=/bin/bash

all: lint test

lint:
	flake8 .
	pydocstyle ../TelegramBots
	isort --check-only .
	mypy .
	echo "done"