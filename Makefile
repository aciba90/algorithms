
test:
	python -m pytest -vv ./src/**/*.py

format:
	python -m black ./src

lint:
	python -m flake8 ./src
