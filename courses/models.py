from django.db import models


class courses(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self):
        return self.full_name


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.CharField(
        max_length=1,
        choices=[
            ('1', '1 - Poor'),
            ('2', '2 - Fair'),
            ('3', '3 - Good'),
            ('4', '4 - Very Good'),
            ('5', '5 - Excellent'),
        ]
    )
    comments = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating})"
