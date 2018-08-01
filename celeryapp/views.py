#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
from tasks import add
# Create your views here.

def run_task(request):
    print('before run add task ')
    result = add.apply_async((1, 2))
    print("redis_key: celery-task-meta-%s" % result)
    print('after run add task')
    return HttpResponse("job is runing background~")


