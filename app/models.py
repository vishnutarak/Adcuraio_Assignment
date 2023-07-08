from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Actors(models.Model):

    username=models.ForeignKey(User,on_delete=models.CASCADE)
    Aname=models.CharField(max_length=100,primary_key=True)
    wekipedia=models.URLField()
    images=models.ImageField()
    NoOfMovies=models.CharField(max_length=100,default=100)

    def __str__(self) -> str:
        return self.Aname