from django.db import models

# Create your models here.


class Feedback(models.Model):
    rating = models.IntegerField(
        default='')
    further_information = models.TextField()

    def __str__(self):
        return self.name
