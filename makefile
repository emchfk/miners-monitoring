.PHONY: lint test typecheck fmt all

fmt:
	uv run ruff format .

lint:
	uv run ruff check . --fix

typecheck:
	uv run mypy --strict src/

test:
	uv run pytest

all: fmt lint typecheck test