from django.contrib import admin
from books.models import Book

# Register your models here.
@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "author",
        "type_book",
        "snippet",
        "need_login",
    ]
    admin.register(Book)
