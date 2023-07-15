from django.urls import path
from . import views

urlpatterns = [
    path('search/',views.search, name="search"),

    path('project/', views.projects, name="projects"),
    path('', views.loginPage, name="login"),
]