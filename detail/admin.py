from django.contrib import admin
from .models import Board, Img, Kakao, Analysis
# Register your models here.

class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('review',)

class BoardAdmin(admin.ModelAdmin):
    list_display = ('destination', 'title', 'contents', 'scope')

class ImgAdmin(admin.ModelAdmin):
    list_display = ('destination', 'address')

class KakaoAdmin(admin.ModelAdmin):
    list_display = ('destination', 'x','y')

admin.site.register(Board, BoardAdmin)
admin.site.register(Img, ImgAdmin)
admin.site.register(Kakao, KakaoAdmin)
admin.site.register(Analysis, AnalysisAdmin)