from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ("id", "email", "first_name", "last_name", "username", "password", "fullname")
   search_fields = ["email", "first_name", "last_name", "username","fullname"]
