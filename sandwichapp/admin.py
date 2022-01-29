from django.contrib import admin
from .models import Bread, Topping, Cheese, Sauce, Sandwich

# Register your models here.

admin.site.register(Bread)
admin.site.register(Topping)
admin.site.register(Cheese)
admin.site.register(Sauce)
admin.site.register(Sandwich)

