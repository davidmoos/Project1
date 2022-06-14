from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name="newpage"),
    path("editpage/<str:title>", views.editpage, name="editpage"),
    path("randompage", views.randompage, name="randompage"),
    path("search", views.search, name="search"),
    path("<str:title>", views.title, name="title"),




]
