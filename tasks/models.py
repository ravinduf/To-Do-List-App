from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    created_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def addTime(self):
        created_date=timezone.now()