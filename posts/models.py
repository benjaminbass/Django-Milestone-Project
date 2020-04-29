from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    service_name = models.CharField(
        max_length=254,
        default='')
    name = models.CharField(
        max_length=254,
        default='')
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    deadline = models.CharField(
        max_length=20,
        default='')
    tag = models.CharField(
        max_length=30,
        default='')
    image = models.ImageField(
        upload_to='images')
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now)
    

    def __str__(self):
        return self.name
