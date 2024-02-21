from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class food(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    type = models.CharField(max_length=100)
    # nutrients = models.FloatField()
    vitamins = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img',blank=True)
    # fav=models.ManyToManyField(User,related_name='favs',blank=True,default=False)
    def __str__(self):
        return self.name

class track(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    # nutrients = models.FloatField()
    vitamins = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img',blank=True)

    # def __str__(self):
    #     return self.name