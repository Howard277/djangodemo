from django.conf.urls import url

from . import HelloController
from . import UserController

urlpatterns = [
    url(r'^hello$', HelloController.hello),
    url(r'^hi$', HelloController.hi),
    url(r'^user/add$',UserController.add),
    url(r'^user/deleteall$',UserController.deleteAll),
]