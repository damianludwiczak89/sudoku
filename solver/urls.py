from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("play/<str:difficulty>", views.play, name="play"),
    path("check_answer", views.check_answer, name="check_answer"),
    path("solution", views.solution, name="solution"),   
]