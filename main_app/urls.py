from django.contrib import admin
from django.urls import path, include

from main_app import views

urlpatterns = [
    path('', views.index),
    path('get-tweets', views.get_tweets)
]