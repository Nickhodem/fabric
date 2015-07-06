from django.db import models
from django.utils import timezone

class Tutor(models.Model):
    name=models.CharField(max_length=25, unique=False)
    surname=models.CharField(max_length=30, unique=False)
    actitle=models.CharField(max_length=50) #academic title
    email=models.EmailField()
    def __unicode__(self):
        return self.name


class Course(models.Model):
    title=models.CharField(max_length=128, unique=False)
    tutor=models.ForeignKey(Tutor, null=True)
    start_date=models.DateField()
    finish_date=models.DateField()
    price=models.FloatField()
    place=models.CharField(max_length=500)
    vacancy=models.IntegerField()
    registration=models.DateField()
    essence=models.TextField()

    def __unicode__(self):
        return self.title

class Student(models.Model):
    name=models.CharField(max_length=25, unique=False)
    surname=models.CharField(max_length=30, unique=False)
    hashname=models.CharField(max_length=30, unique=True)
    email=models.EmailField(unique=True)
    paid=models.BooleanField(default=False)
    registered_day=models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.hashname


