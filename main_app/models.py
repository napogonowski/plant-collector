from django.db import models
from django.urls import reverse


class Plant(models.Model):
    givenName = models.CharField(max_length=100)
    plantName = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    potSize = models.CharField(max_length=5)
    height = models.IntegerField()

    def __str__(self):
        return f'{self.givenName} ({self.id})'


    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})