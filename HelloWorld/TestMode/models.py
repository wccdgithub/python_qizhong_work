from django.db import models
 
class pq(models.Model):
    title = models.CharField(max_length=20)
    urls = models.CharField(max_length=1000)
    objects=models.Manager()

class weather(models.Model):
    city = models.CharField(max_length=20)
    date= models.CharField(max_length=20)
    weather = models.CharField(max_length=20)
    temp= models.CharField(max_length=20)
    objects=models.Manager()

class phone(models.Model):
    mark = models.CharField(max_length=100)
    price= models.CharField(max_length=20)
    img_index = models.CharField(max_length=100)

    objects=models.Manager()