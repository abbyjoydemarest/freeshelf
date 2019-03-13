from django.contrib import admin
from core.models import Book, Author, Category

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CatergoryAdmin(admin.ModelAdmin):
    pass
