from django.contrib import admin
from .models import task
# Register your models here.
@admin.register(task)

class postModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'complete', 'created']