from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'is_bot', 'date_joined')
    search_fields = ('user_id', 'username', 'email')