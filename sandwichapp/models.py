from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE

# Create your models here.

class Bread(SafeDeleteModel):
    _safedelete_policy=SOFT_DELETE
    name = models.CharField(max_length=255, unique=True)
    inventory_count = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.name} 가격{self.price} 남은갯수{self.inventory_count}'

class Topping(SafeDeleteModel):
    _safedelete_policy=SOFT_DELETE
    name = models.CharField(max_length=255, unique=True)
    inventory_count = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.name} 가격{self.price} 남은갯수{self.inventory_count}'    

class Cheese(SafeDeleteModel):
    _safedelete_policy=SOFT_DELETE
    name = models.CharField(max_length=255, unique=True)
    inventory_count = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.name} 가격{self.price} 남은갯수{self.inventory_count}'

class Sauce(SafeDeleteModel):
    _safedelete_policy=SOFT_DELETE
    name = models.CharField(max_length=255, unique=True)
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

    def __str__(self):
        return f'{self.bread}{list(self.toppings.all())}{self.cheese}{list(self.sauces.all())} '


