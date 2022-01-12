from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.forms import IntegerField


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = ArrayField(models.CharField(max_length=100))
    total_copies = models.IntegerField(default=0)
