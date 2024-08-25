from django.contrib import admin

# Register your models here
from .models import CustomUser

@admin.register(CustoUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
