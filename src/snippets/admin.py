from django.contrib import admin
from snippets.models import Snippet

# Register your models here.
@admin.register(Snippet)
class Snippet(admin.ModelAdmin):
    list_display = ["created", "title", "code", "linenos", "language", "style"]
    admin.register(Snippet)
