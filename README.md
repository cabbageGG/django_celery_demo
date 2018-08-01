# django_celery_demo
A demo to create Asynchronous task and Timed task


 
requirement:
  django >= 1.8
  celery >= 4.2

sudo apt-get install redis-server

start:
   1.start django project
     python manage.py runserver
   2.start celery worker
     python -A django_celery_demo worker
   3.start celery beat
     python -A django_celery_demo beat

feature:
   1.call url to ceate Asynchronous task
       127.0.0.1:8000/celery/1/
   2.Timed task is also allowed
