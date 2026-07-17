.PHONY: check test test-slow test-all lint structure

check: lint test

test:
	python -m pytest

test-slow:
	python -m pytest -m slow

test-all:
	python -m pytest -m "slow or not slow"

lint:
	python -m ruff check .

structure:
	python -m pytest tests/test_repository_structure.py
