from django.db import models

class Event(models.Model):
    event_image = models.ImageField(upload_to='images/')
    primary_heading = models.CharField(max_length=40)
    secondary_heading = models.CharField(max_length=50)
    event_description = models.CharField(max_length=500)
    