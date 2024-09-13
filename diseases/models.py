from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    symptoms = models.TextField()
    treatments = models.TextField()

    def __str__(self):
        return self.name