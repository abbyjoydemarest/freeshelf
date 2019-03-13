from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    
    author = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.author)


class Category(models.Model):

    book_category = models.CharField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.book_category)

class Book(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library.)"""
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    author = models.ManyToManyField(Author)
    description = models.TextField(null=True, blank=True)
    access_online = models.URLField(max_length=200, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=True, blank=True)
    book_category = models.ManyToManyField(Category)

    class Meta: 
        ordering = ['-date_added']


    def __str__(self):
        return str(self.title)
    

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.slug)])
