from django.db import models
from django.conf import settings

from heartcenter.settings import LANGUAGE_CHOICES

class Doctor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    text = models.TextField()
    lang = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.name
