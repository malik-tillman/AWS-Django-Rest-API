from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    importance = models.CharField(max_length=1)
    level = models.CharField(max_length=1)
    keywords = ArrayField(models.CharField(max_length=50))
    summary = models.TextField()
    languages = ArrayField(models.CharField(max_length=50))
    media = models.CharField(max_length=200)

    def __str__(self):
        return self.name
