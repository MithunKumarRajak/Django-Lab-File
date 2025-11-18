from django.db import models


class Course(models.Model):
    courseName = models.CharField(max_length=100)
    courseFee = models.FloatField()
    courseInstructor = models.CharField(max_length=100)

    def __str__(self):
        return self.courseName


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name="students")

    def __str__(self):
        return self.name
