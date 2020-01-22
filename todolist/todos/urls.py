from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    url('details/(?P<id>\w{0,50})/', views.details ),
    url('add/(?P<id>\w{0,50})/', views.add ),
   
]
