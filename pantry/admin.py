from django.contrib import admin
from .models import PantryItem

@admin.register(PantryItem)
class PantryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at', 'updated_at')
    search_fields = ('name', 'user__username')