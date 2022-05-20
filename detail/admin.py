from django.contrib import admin
from .models import Board
# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'contents', 'scope')

admin.site.register(Board, SearchAdmin)