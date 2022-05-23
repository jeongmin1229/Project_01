from django.db import models

# Create your models here.

# class Img(models.Model):
#     destination = models.ForeignKey('search.Search', on_delete=models.CASCADE, verbose_name='목적지')
#     address = models.CharField(max_length=500, verbose_name='이미지 주소')

#     class Meta:
#         verbose_name = "이미지"
#         verbose_name_plural = "이미지"


class Board(models.Model):
    # destination = models.ForeignKey('search.Search', on_delete=models.CASCADE, verbose_name='목적지')  
    title = models.CharField(max_length=150 ,verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    scope = models.CharField(max_length=10, verbose_name='별점')
    register_dttm = models.CharField(max_length=100, verbose_name='등록날짜') # 등록날짜인데 누구랑 동행했는지도 나와서

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰"

    def __str__(self):
        return self.title

   
