from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)


    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=120)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Location(models.Model):
    latitude = models.DecimalField(max_digits=20, decimal_places=11)
    longitude = models.DecimalField(max_digits=20, decimal_places=11)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_location')
