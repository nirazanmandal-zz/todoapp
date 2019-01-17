from django.conf.urls import url
from . import views

app_name = "todo"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^list/$', views.list, name='list'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),

]
