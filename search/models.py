from ctypes import addressof
from django.db import models

class Searchdata(models.Model):
    title = models.CharField()
    address = models.CharField()
    url = models.CharField()
    image = models.CharField()