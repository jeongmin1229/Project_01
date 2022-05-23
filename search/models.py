from django.db import models

class Search(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    url = models.TextField()
    image = models.TextField()
    review_count = models.CharField(max_length=200,default="")
    rating = models.CharField(max_length=200,default="")
# Create your models here.
