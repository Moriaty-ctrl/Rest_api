from django.db import models

# Create your models here.



class Movie(models.Model):
    movie =models.CharField(max_length=10)
    hall =models.CharField(max_length=10)
    date =models.DateField()

class Guest(models.Model):
    name =models.CharField(max_length=20)
    mobile =models.CharField(max_length=10)


class Reservation(models.Model):
    guest =models.ForeignKey(Guest,related_name='reservation', on_delete=models.CASCADE)
    movie =models.ForeignKey(Movie,related_name='reservation', on_delete=models.CASCADE)

