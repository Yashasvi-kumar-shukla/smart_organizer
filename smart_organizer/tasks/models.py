from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    deadline = models.DateTimeField(default=now)
    priority = models.CharField(max_length=50, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    is_complete = models.BooleanField(default=False)  # Ensure this field exists
    def __str__(self):
        return self.title