from django.contrib import admin
from .models import User, Expense, Income

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'password']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'time', 'amount', 'remark', 'category', 'user_id']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'time', 'amount', 'remark', 'category', 'user_id']