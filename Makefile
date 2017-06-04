init:
	pip install -r requirements.txt

test:
	nosetests tests
	
testLettuce:
	cd tests
	lettuce
	cd ..

coverage:
	coverage run sample/core.py
	coverage report -m