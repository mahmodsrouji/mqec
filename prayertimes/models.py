# prayer/models.py
from django.db import models

class PrayerTime(models.Model):
    date = models.DateField(unique=True)
    fajr = models.TimeField()
    dhuhr = models.TimeField()
    asr = models.TimeField()
    maghrib = models.TimeField()
    isha = models.TimeField()

    def __str__(self):
        return f"Prayer Times for {self.date}"
