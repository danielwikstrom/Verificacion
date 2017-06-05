init:
	pip install -r requirements.txt

test:
	nosetests tests
	cd tests; \
	lettuce; 
	
runServer:
	python manage.py runserver &
	python manage.py migrate &

coverage:
	coverage run sample/core.py
	coverage report -m