from django.contrib import admin
from .models import Board, Img
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'contents', 'scope')

class ImgAdmin(admin.ModelAdmin):
    list_display = ('address',)

admin.site.register(Board, BoardAdmin)
admin.site.register(Img, ImgAdmin)