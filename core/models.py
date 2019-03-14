from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    
    author = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.author


class Category(models.Model):

    book_category = models.CharField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        return self.book_category

class Book(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library.)"""
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ManyToManyField(Author)
    description = models.TextField(null=True, blank=True)
    access_online = models.URLField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=True, blank=True)
    book_category = models.ManyToManyField(Category)


    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)


    def set_slug(self):
        #If the slug is already set, stop here.
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        while Book.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)

        self.slug = slug


    class Meta: 
        ordering = ['-date_added']


    def __str__(self):
        return str(self.title)
    

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.slug)])
