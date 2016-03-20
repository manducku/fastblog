#clean cache 
clean:
	find . -name "*.pyc" -exec rm -rf {} \;
#migrate posts, user model 
migrate:
	python fastblog/manage.py makemigrations posts 
	python fastblog/manage.py migrate
#test posts, users 
test:
	python fastblog/manage.py test posts  

