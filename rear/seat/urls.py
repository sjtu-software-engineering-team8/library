from django.conf.urls import url
from django.contrib import admin
from seat import views
from django.conf.urls import include

urlpatterns = [
    url(r'^', views.get_use_all_seat),
]