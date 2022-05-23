from django.db import models

class Search(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    url = models.CharField(max_length= 200)
    image = models.CharField(max_length=200)
    
    
    # Create your models here.

    class Meta:
            verbose_name = "검색"
            verbose_name_plural = "검색"

    def __str__(self):
        return self.title
