from django.db import models

# Create your models here.
class TravelPage(models.Model):
    Name= models.CharField(max_length=100)
    whether=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    Description= models.TextField()
