from django.db import models

# Create your models here.

class Hobby(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Person(models.Model):
    
    name = models.CharField(max_length=100)
    hobbies = models.ManyToManyField(Hobby)

    def __str__(self):
        return self.name

