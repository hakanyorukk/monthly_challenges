from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Months(models.Model):
    month = models.CharField(max_length=12)
    slug = models.SlugField(null=False, unique=True)
    def months(self):
        return f"{self.month}"
    
    def __str__(self):
        return self.months()

class Challenges(models.Model):
    challenge = models.CharField(max_length=100)
    month = models.ForeignKey(Months, on_delete=models.CASCADE)