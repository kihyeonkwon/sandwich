from rest_framework import serializers


from sandwichapp.models import Bread, Topping, Cheese, Sauce, Sandwich


class BreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bread
        fields = '__all__'
        

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'
        
class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = '__all__'
        
class SauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sauce
        fields = '__all__'
        
class SandwichSerializer(serializers.ModelSerializer):
    class BreadSerializer(serializers.ModelSerializer):
        class Meta:
            model = Bread
            fields = ['name', 'price']
            ref_name="Sandwich Bread"
    
    class ToppingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Topping
            fields = ['name', 'price']
            ref_name="Sandwich Topping"
            
    class CheeseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Cheese
            fields = ['name', 'price']
            ref_name="Sandwich Cheese"
            
    class SauceSerializer(serializers.ModelSerializer):
        class Meta:
            model = Sauce
            fields = ['name', 'price']
            ref_name="Sandwich Sauce"

    bread = BreadSerializer(read_only=True)
    toppings = ToppingSerializer(many=True, read_only=True)
    cheese = CheeseSerializer(read_only=True)
    sauces = SauceSerializer(many=True, read_only=True)

    class Meta:
        model = Sandwich
        fields=['id','bread','toppings', 'cheese', 'sauces', 'price']


