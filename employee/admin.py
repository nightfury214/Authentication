from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
   list_display = ("name", "position", "email", "salary", "createBy")
   search_fields = ["name", "position", "email", "salary", "createBy"]
