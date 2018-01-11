from django.shortcuts import render
from TestModel.models import Role

def add(request):
    # user1=User(name='wuketao',age=33)
    # user1.save()
    role1 = Role(code='001',name='admin',description='he is admin')
    role1.save()
    return render(request,'user/add.html',None)

def deleteAll(request):
    Role.objects.all().delete()
    return render(request,'user/delete.html',None)

