install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build