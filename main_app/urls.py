from django.urls import path

from main_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get-tweets", views.get_tweets),
    path("account/<username>", views.get_account_details, name="account-page"),
]
