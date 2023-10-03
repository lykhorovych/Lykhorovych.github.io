from django.urls import path
from .views import AddTon, ListTon, index

urlpatterns = [
    path("", index, name='base'),
    path("add/", AddTon.as_view(), name='add'),
    path("all/", ListTon.as_view(), name='all'),
]