from .models import Feedback
from django.contrib import admin
from .models import courses

# Register your models here.
admin.site.register(courses)
admin.site.register(Feedback)
