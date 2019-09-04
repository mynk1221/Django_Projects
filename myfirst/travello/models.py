from django.db import models

# Create your models here.

class Destination(models.Model):
    # id = int  #in database primary key is automatically generated
    # name : str for str int database we use below method
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)