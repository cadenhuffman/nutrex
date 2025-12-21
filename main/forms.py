from django.forms import ModelForm
from .models import Workout, Cluster, Exercise
from django.contrib.auth.models import User


class WorkoutForm(ModelForm):

    class Meta:
        model = Workout
        fields = ["date", "duration_mins"]



class ClusterForm(ModelForm):

    class Meta:
        model = Cluster
        fields = ["sets", "reps", "weight", "exercise"]
        
        

class ExerciseForm(ModelForm):

    class Meta:
        model = Exercise
        fields = ["name", "primary_muscle"]



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
