install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

selfcheck:
	poetry check

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

check: selfcheck test lint

.PHONY: install test lint selfcheck check build