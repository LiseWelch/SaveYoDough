from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.root),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^password$', views.password),
    url(r'^username$', views.username),
    url(r'^email$', views.email),
    url(r'^lastname$', views.lastname),
    url(r'^firstname$', views.firstname),
    url(r'^register$', views.register),
    url(r'^confirm$', views.confirm),
]



