from django.conf.urls import url
from django.contrib import admin
from credit import views
from django.conf.urls import include

urlpatterns = [
    url(r'$', views.credit),
]