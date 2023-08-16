from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Months(models.Model):
    month_name = models.CharField(max_length=12)
    slug = models.SlugField(default="", null=False, unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug =slugify(self.month_name)
        super().save(*args, **kwargs)

    def months(self):
        return f"{self.month_name}"
    
    def __str__(self):
        return self.month_name

class Challenges(models.Model):
    challenge = models.CharField(max_length=100)
    months = models.ForeignKey(Months,null=True, on_delete=models.CASCADE, related_name="months")

    def challenges(self):
        return f"{self.challenge}"

    def __str__(self):
        return self.challenge