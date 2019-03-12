from django.contrib import admin
from core.models import Book, Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ('slug',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
