from django.db import models
from django.urls import reverse
from datetime import date, timedelta

FEEDS = (
    ('W', 'Water'),
    ('F', 'Liquid Fertiliser'),
    ('T', 'Plant Tonics'),
)
POT_SIZE = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('X', 'Extra Large'),
)


class Extra(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('extras_detail', kwargs={'pk': self.id})


class Plant(models.Model):
    givenName = models.CharField(
        'Plant Name',
        max_length=100)
    plantName = models.CharField(
        'Plant Type',
        max_length=100)
    description = models.TextField(max_length=250)
    potSize = models.CharField(
        'Pot Size',
        max_length=1,
        choices=POT_SIZE,
        default=POT_SIZE[0][0]
    )
    height = models.IntegerField('Height (cm)')
    extras = models.ManyToManyField(Extra)

    def __str__(self):
        return f'{self.givenName} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

    def fed_for_the_week(self):
        today = date.today()
        last_week = today - timedelta(weeks=1)
        is_fed = self.feeding_set.filter(date__gte=last_week).count()
        print(is_fed)
        return is_fed


class Feeding(models.Model):
    date = models.DateField('feeding date')
    feed = models.CharField(
        'feed type',
        max_length=1,
        choices=FEEDS,
        default=FEEDS[0][0]
    )
    # FK
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_feed_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
