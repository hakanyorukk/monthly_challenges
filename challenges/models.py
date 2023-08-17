from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Challenges(models.Model):
    challenge = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f"{self.challenge}"
    
class Months(models.Model):
    month_name = models.CharField(max_length=12)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    challenge = models.ForeignKey(Challenges,null=True, on_delete=models.CASCADE, related_name="months")

    def save(self, *args, **kwargs):
       self.slug = slugify(self.month_name)
       super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("month_challenge", args=[self.slug])

    def __str__(self):
        return f"{self.month_name}"
    
    
