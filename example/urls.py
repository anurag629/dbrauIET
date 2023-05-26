# example/urls.py
from django.urls import path

from example.views import index

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index),
]

urlpatterns += staticfiles_urlpatterns()