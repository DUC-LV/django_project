from django.contrib import admin
from books.models import Book

# Register your models here.
@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = [
        "created",
        "name",
        "price",
        "author",
        "type_book",
        "snippet",
        "need_login",
        "image_cover",
    ]
    admin.register(Book)
