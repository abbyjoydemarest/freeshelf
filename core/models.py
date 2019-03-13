from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library.)"""
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    access_online = models.URLField(max_length=200, null=True, blank=True)
    date_added = models.DateField(null=True, blank=True)
    book_category = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['-date_added']


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.slug)])

class Author(models.Model):
    pass
    #author = models.ManyToManyField(Book)


    #def __str__(self):
    #    return self.name


class Category(models.Model):
    pass
    #book_category = models.ManyToManyField(Book)
    

   # def __str__(self):
    #    return self.book_category

