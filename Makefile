.PHONY: install
install:
	pip install -r requirements.txt

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