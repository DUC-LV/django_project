from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from polls.models import Company

def getJson(request):
    obj = Company.objects.all()
    data = { "result" :list(obj.values("_id", "name", "age", "adress", "salary", "join_date"))
            }
    return JsonResponse(data)