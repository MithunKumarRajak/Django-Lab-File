from django.db import models
# Create your models here.
# Scheme== models


class User(models.Model):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    course = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name

