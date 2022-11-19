from django.db import models

class Company(models.Model):
    _id = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    age = models.IntegerField(null=True, blank=False)
    adress = models.CharField(null=True, blank=False, max_length=500)
    salary = models.IntegerField(null=True, blank=False)
    join_date = models.DateTimeField(null=False, blank=False)
    
    @classmethod
    def Create(cls, _id, name, age, adress,salary, join_date):
        test_record = cls(_id=_id, name=name, age=age, adress=adress, salary=salary, join_date=join_date)
        return test_record

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
