from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
