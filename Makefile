
test:
	python -m pytest -v ./src/**/*.py

format:
	python -m black ./src

lint:
	python -m flake8 ./src
