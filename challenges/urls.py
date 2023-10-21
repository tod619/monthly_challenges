from django.urls import path

from . import views


urlpatterns = [
    path("janurary", views.janurary),
    path("february", views.february)
]