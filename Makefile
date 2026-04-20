install:
	pip install -e .

test:
	python -m pytest -vv

lint:
	flake8 gendiff

.PHONY: install test lint