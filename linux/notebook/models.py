from django.db import models

class Names(models.Model):
    number = models.IntegerField()
    name = models.JSONField()

    def __str__(self):
        return self.number