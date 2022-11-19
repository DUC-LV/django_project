from rest_framework import serializers
from polls.models import Company

class CompanySerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
                model = Company
                fields = ('_id', 'name', 'age', 'adress', 'salary', 'join_date')