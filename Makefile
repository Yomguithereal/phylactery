# Variables
SOURCE = phylactery

# Commands
all: lint test
test: unit
publish: lint test upload clean

clean:
	rm -rf *.egg-info .pytest_cache ./**/__pycache__ build dist
	find . -name "*.pyc" | xargs rm

lint:
	@echo Linting source code using pep8...
	pycodestyle --ignore E402,E501 $(SOURCE) test
	@echo

unit:
	@echo Running unit tests...
	pytest -s
	@echo

upload:
	python setup.py sdist bdist_wheel
	twine upload dist/*
