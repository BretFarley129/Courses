from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^(?P<number>\d+)/destroy$', views.destroy),
    url(r'^(?P<number>\d+)/delete$', views.delete)
]