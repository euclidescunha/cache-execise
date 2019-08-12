.SILENT:
.PHONY: clean


unit:
	echo "\n\n RUNNING UNIT TESTS"
	export PYTHONPATH=${PYTHONPATH}:src && pytest

start:
	export PYTHONPATH=${PYTHONPATH}:src && gunicorn web.start:app

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

setup:
	pipenv install
