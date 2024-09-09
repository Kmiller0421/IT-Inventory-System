from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("adminLogin.html", views.adminLogin, name="adminLogin"),
    path("base.html", views.base, name="base"),
    path("forgotPage.html", views.forgotPage, name="forgotPage"),
    path("forgotPageSuccessful.html", views.forgotPageSuccessful, name="forgotPageSuccessful"),
]