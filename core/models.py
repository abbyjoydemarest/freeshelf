from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library.)"""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    access_online = models.CharField(max_length=200)
    date_added = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
