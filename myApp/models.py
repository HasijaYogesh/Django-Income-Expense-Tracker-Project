from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    class Meta:
        db_table = 'user'

class Expense(models.Model):
    date = models.DateField()
    time = models.TimeField()
    amount = models.FloatField()
    remark = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'expense'

class Income(models.Model):
    date = models.DateField()
    time = models.TimeField()
    amount = models.FloatField()
    remark = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'income'