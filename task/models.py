from django.db import models
from django.utils import timezone

class Task(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(null=True, blank=True)
