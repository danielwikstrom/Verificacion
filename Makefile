init:
	pip install -r requirements.txt

test:
	nosetests tests
	python manage.py runserver 
	cd tests; \
	lettuce; 

	

coverage:
	coverage run sample/core.py
	coverage report -m