.PHONY: data
.EXPORT_ALL_VARIABLES:

environment: data 
	@echo "Installing..."
	poetry install
	poetry run pre-commit install

data: 
	@echo "Downloading data..."
	wget -P data/raw https://gist.githubusercontent.com/khuyentran1401/5832beb560b208224c4a0c849e7332f0/raw/1965f7c1fa4fd222da5284e28f08bd2ac99e5b0e/winequality-red.csv

activate:
	@echo "Activating virtual environment..."
	poetry shell

test:
	pytest