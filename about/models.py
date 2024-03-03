from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    title = model.CharField(max_length=200, unique=True)
    Content = model.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
