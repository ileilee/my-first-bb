from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cust_list, name='cust_list'),
]