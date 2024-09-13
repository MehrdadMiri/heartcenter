from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    uses = models.TextField()
    side_effects = models.TextField()

    def __str__(self):
        return self.name