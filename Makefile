.PHONY: build test lint clean

build:
	python setup.py sdist bdist_wheel

test:
	pytest --maxfail=1 --disable-warnings -q

lint:
	flake8 demo_project tests

clean:
	rm -rf build dist *.egg-info
	find . -type d -name '__pycache__' -exec rm -rf {} +
