from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import Role
from . import JsonTools

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def hi(request):
    user1 = Role(code='001',name='admin')
    return HttpResponse(JsonTools.MyEncoder().encode(user1))

