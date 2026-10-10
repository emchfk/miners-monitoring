.PHONY: lint test typecheck fmt doc all

fmt:
	uv run ruff format .

lint:
	uv run ruff check . --fix

typecheck:
	uv run mypy --strict src/

test:
	uv run pytest

doc:
	uv run mkdocs build

all: fmt lint typecheck test