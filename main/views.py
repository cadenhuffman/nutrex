from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .forms import *
from .models import *

# Create your views here.



def index(request):
    return render(request, "main/index.html")



def add_workout(request):
    if request.method == "POST":

        form = WorkoutForm(request.POST)

        if form.is_valid():
            duration_mins = form.cleaned_data["duration_mins"]
            date = form.cleaned_data["date"]

            new_workout = Workout.objects.create(date = date, duration_mins = duration_mins)


            
            return HttpResponseRedirect(reverse('add_cluster', args = (new_workout.id,)))


    else:
        form = WorkoutForm()

    return render(request, "main/add_workout.html", {"form":form})


def add_cluster(request, workout_id):
    if request.method == "POST":

        form = ClusterForm(request.POST)



        if form.is_valid():
            reps = form.cleaned_data["reps"]
            sets = form.cleaned_data["sets"]
            weight = form.cleaned_data["weight"]
            exercise = form.cleaned_data["exercise"]
            workout = Workout.objects.get(id = workout_id)
            new_cluster = Cluster.objects.create(reps = reps, sets = sets, weight = weight, 
                                                exercise = exercise, workout = workout )

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('add_cluster', args = (workout_id,)))



    else:
        form = ClusterForm()


    return render(request ,"main/add_exercises.html", {"form":form})

    


            


    
