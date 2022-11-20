from rest_framework import serializers
from books.models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "price",
            "author",
            "type_book",
            "snippet",
            "need_login",
            "image_cover",
        ]