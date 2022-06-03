from django.db import models

class Names(models.Model):
    name = models.JSONField()
