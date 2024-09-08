from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("struct.html", views.struct, name="struct"),
    path("base.html", views.base, name="base"),
]