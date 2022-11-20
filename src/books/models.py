from django.db import models

# Create your models here.
class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    author = models.CharField(max_length=100)
    type_book = models.CharField(max_length=200)
    snippet = models.TextField()
    need_login = models.IntegerField(default=0)
    image_cover = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['created']
    # def __str__(self):
    #     return self.title