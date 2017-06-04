init:
	pip install -r requirements.txt

test:
	nosetests tests
	START "" python manage.py runserver 
	cd tests; \
	lettuce; 

	

coverage:
	coverage run sample/core.py
	coverage report -m