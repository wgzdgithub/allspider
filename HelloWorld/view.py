# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = dict()
    context['hello'] = 'Hello World!'
    context['name'] = 'what is your name?'
    context['age'] = 'what is your age'
    context['num'] = 'which is this number?'
    context['li'] = 'why can wrong?'
    return render(request, 'hello.html', context)


def name(request):
    var1 = dict()
    var1["name"] = 'wgz'
    return render(request, 'name.html', var1)


def age(request):
    var2 = dict()
    var2['age'] = '王光兆2222222'
    return render(request, 'age.html', var2)
