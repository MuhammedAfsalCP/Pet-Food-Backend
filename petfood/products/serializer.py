from rest_framework import serializers

from .models import Products


class ProductsSeriealizer(serializers.ModelSerializer):

    class Meta:
        model=Products
        fields=('Name','Category','Price','Description','Brand','Weight','Stock','Image','Ingredient')


    def validate_Price(self,value):
        if value<=0:
            raise serializers.ValidationError(
            "price must be greater than zero"
            )

        return value
    