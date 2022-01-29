from django.db import models

# Create your models here.

class Bread(models.Model):
    name = models.CharField(max_length=255)
    inventory_count = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.name} 가격{self.price} 남은갯수{self.inventory_count}'

class Topping(models.Model):
    name = models.CharField(max_length=255)
    inventory_count = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.name} 가격{self.price} 남은갯수{self.inventory_count}'    

class Cheese(models.Model):
    name = models.CharField(max_length=255)
    inventory_count = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.name} 가격{self.price} 남은갯수{self.inventory_count}'

class Sauce(models.Model):
    name = models.CharField(max_length=255)
    inventory_count = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.name} 가격{self.price} 남은갯수{self.inventory_count}'

class Sandwich(models.Model):
    bread = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    toppings = models.ManyToManyField(Topping)
    cheese = models.ForeignKey(Cheese, on_delete=models.DO_NOTHING)
    sauces = models.ManyToManyField(Sauce)
    price = models.IntegerField()


