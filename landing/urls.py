from django.contrib import admin
from django.conf.urls import url, include
from landing import views

urlpatterns = [
    url(r'^landing/', views.landing, name='landing'),
]
