from django.db import models

from heartcenter.settings import LANGUAGE_CHOICES

class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    symptoms = models.TextField()
    treatments = models.TextField()
    lang = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.name
