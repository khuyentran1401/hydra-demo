.PHONY: notebook docs
.EXPORT_ALL_VARIABLES:

install: 
	@echo "Installing..."
	poetry install
	poetry run pre-commit install

download_data:
	@echo "Download data..."
	wget -P data/raw https://gist.githubusercontent.com/khuyentran1401/5832beb560b208224c4a0c849e7332f0/raw/e4534825f9aef4c26f072d6f1226a40c5b47c27c/winequality-red.csv

setup: install download_data

activate:
	@echo "Activating virtual environment"
	poetry shell

test:
	pytest