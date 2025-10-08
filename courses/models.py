from django.db import models

# Create your models here.


class courses(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self):
        return self.full_name
