from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile/%Y/%m/%d', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Kontakt(models.Model):
    name=models.CharField(max_length=50, blank=False)
    email=models.EmailField(blank=False)
    message=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.name