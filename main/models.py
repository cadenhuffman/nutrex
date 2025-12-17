from django.db import models

# Create your models here.


class Muscle(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name



class Exercise(models.Model):
    name = models.CharField(max_length = 200)
    primary_muscle = models.ForeignKey(Muscle, on_delete = models.CASCADE)

    def __str__(self):
        return self.name



class Workout(models.Model):
    date = models.DateField()
    duration_mins = models.IntegerField()
    #total_volume = computed 


class Cluster(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete = models.CASCADE)
    weight = models.IntegerField()
    reps = models.IntegerField()
    sets = models.IntegerField()
    workout = models.ForeignKey(Workout, on_delete = models.CASCADE)


    def __str__(self):
        return f"{self.exercise} at {self.weight} for {self.reps} x {self.sets}"


