from django.db import models


class Student(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.roll_no} - {self.name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="books", null=True, blank=True)

    def __str__(self):
        return self.title
