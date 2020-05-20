from django.urls import path

from main_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get-tweets", views.get_account),
    path("account/<username>/", views.generate_report, name="account-page"),
    path("account/<username>/<int:tweets>", views.generate_report, name="account-page"),
]
