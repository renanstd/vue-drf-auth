from django.contrib import admin
from core import models


@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'done', 'date']
    list_filter = ['done']
    ordering = ['name']
