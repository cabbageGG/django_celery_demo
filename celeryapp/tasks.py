# create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time


@shared_task(name="add-func")
def add(x, y):
    print "++++++++++++++++++++++++++++++++++++"
    print('job is running....')
    time.sleep(5)
    print('job is done')
    return x + y

