from django.contrib import admin

# Register your models here.
from .models import tasks

admin.site.register(tasks)