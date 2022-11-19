from django.contrib import admin
from polls.models import Company


# Register your models here.
@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ["_id", "name", "age", "salary", "adress", "join_date"]
    admin.register(Company)