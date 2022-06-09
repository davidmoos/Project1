from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name="newpage"),
    path("search", views.search, name="search"),
    path("<str:title>", views.title, name="title"),


]
