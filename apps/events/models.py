from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)

    def __str__(self):
        return self.title