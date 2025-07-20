from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these fields in the list view
    list_filter = ('publication_year', 'author')  # allow filtering by these fields
    search_fields = ('title', 'author')  # enable search by title or author
