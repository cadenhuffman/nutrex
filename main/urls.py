from django.urls import path
from . import views




urlpatterns = [
    path("", views.index, name = "index"),
    path("add_workout", views.add_workout, name = "add_workout"),
    path("<int:workout_id>/add_exercise", views.add_cluster, name = "add_cluster")
]