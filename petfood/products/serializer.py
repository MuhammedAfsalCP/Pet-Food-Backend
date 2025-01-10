from rest_framework import serializers

from .models import Products


class ProductsSeriealizer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = (
            "id",
            "Name",
            "Category",
            "Price",
            "Description",
            "Brand",
            "Weight",
            "Stock",
            "Image",
            "Ingredient",
        )

    # Validate Product Name
    def validate_Name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Product name cannot be empty or just whitespace."
            )
        return value

    # Validate Price
    def validate_Price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    # Validate Description
    def validate_Description(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Description cannot be empty or just whitespace."
            )
        if len(value) < 10:
            raise serializers.ValidationError(
                "Description must be at least 10 characters long."
            )
        return value

    # Validate Brand
    def validate_Brand(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Brand cannot be empty or just whitespace."
            )
        return value

    # Validate Weight

    # Validate Stock
    def validate_Stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value

    # Validate Ingredients
    def validate_Ingredients(self, value):
        # Ensure that the value is a list
        if not isinstance(value, list):
            raise serializers.ValidationError("Ingredients must be a list.")
        return value

    # Validate Category
    def validate_Category(self, value):
        if value not in ["Cat", "Dog"]:
            raise serializers.ValidationError("Category must be either 'Cat' or 'Dog'.")
        return value

    # Validate Image
    def validate_Image(self, value):
        if value is None:
            raise serializers.ValidationError("Image is required.")
        return value
