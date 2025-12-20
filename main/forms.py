from django.forms import ModelForm
from .models import Workout, Cluster



class WorkoutForm(ModelForm):

    class Meta:
        model = Workout
        fields = ["date", "duration_mins"]



class ClusterForm(ModelForm):

    class Meta:
        model = Cluster
        fields = ["sets", "reps", "weight", "exercise"]
        
        


