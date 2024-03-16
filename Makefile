.PHONY: install
install:
	pip install -r requirements.txt
	pip install -r ./tests/test_requirements.txt


.PHONY: uninstall
uninstall:
	pip uninstall -y -r <(pip freeze)

.PHONY: run
run:
	uvicorn app.main:app --reload

.PHONY: reset-db
reset-db:
	psql -h localhost -U postgres -c "DROP DATABASE IF EXISTS onlybrands"
	psql -h localhost -U postgres -c "CREATE DATABASE onlybrands"

.PHONY: lint
lint:
	ruff check app/ tests/
	ruff format app/ tests/ --check

.PHONY: format
format:
	ruff check app/ tests/ --fix
	ruff format app/ tests/