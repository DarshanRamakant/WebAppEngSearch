from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.projects, name="projects"),
    path('', views.search, name="search"),
]