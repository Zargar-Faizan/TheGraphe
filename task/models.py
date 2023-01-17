from django.db import models

# Create your models here.
class Movie(models.Model):
    movieName = models.CharField(max_length=100)
    movieDuration = models.CharField(max_length=100,default="")
    def __str__(self):
        return str(self.id)

class Moviedesc(models.Model):
    castname = models.CharField(max_length=100,default="")
    gender = models.CharField(max_length=100,default="")
    charactername = models.CharField(max_length=100,default="")
    movieid = models.ForeignKey("Movie", on_delete=models.CASCADE,default="")
    def __str__(self):
        return str(self.id)


class Moviedialogue(models.Model):
    dialogue = models.CharField(max_length=100,default="")
    starttime = models.CharField(max_length=100,default="")
    endtime = models.CharField(max_length=100,default="")
    movieid = models.ForeignKey("Movie", on_delete=models.CASCADE,default="")
    castid = models.ForeignKey("Moviedesc", on_delete=models.CASCADE,default="")


