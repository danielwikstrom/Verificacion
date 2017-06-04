init:
	pip install -r requirements.txt

test:
	nosetests tests
	cd tests; \
	lettuce; 

	

coverage:
	coverage run sample/core.py
	coverage report -m