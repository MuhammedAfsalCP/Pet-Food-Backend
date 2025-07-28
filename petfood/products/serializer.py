from rest_framework import serializers
from .models import Products
from .utils import upload_image_to_cloudinary

class ProductsSerializer(serializers.ModelSerializer):
    Image = serializers.ImageField(write_only=True, required=True)
    image_url = serializers.URLField(source='Image', read_only=True)

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
            "Image",       # for file upload
            "image_url",   # to return the Cloudinary URL
            "Ingredient",
        )

    

    def validate_Name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Product name cannot be empty or whitespace.")
        return value

    def validate_Price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_Description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Description cannot be empty.")
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters.")
        return value

    def validate_Brand(self, value):
        if not value.strip():
            raise serializers.ValidationError("Brand cannot be empty.")
        return value

    def validate_Stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value

    def validate_Category(self, value):
        if value not in ["Cat", "Dog"]:
            raise serializers.ValidationError("Category must be either 'Cat' or 'Dog'.")
        return value

    def validate_Ingredient(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Ingredient must be a list.")
        return value
    def create(self, validated_data):
        image_file = validated_data.pop('Image', None)

        # Validate image presence
        if not image_file:
            raise serializers.ValidationError("Image file is required.")
    
        # Validate MIME type
        allowed_types = ['image/jpeg', 'image/png', 'image/webp']
        content_type = getattr(image_file, 'content_type', None)
    
        if content_type not in allowed_types:
            raise serializers.ValidationError(f"Unsupported image type: {content_type}")
    
        # Upload to Cloudinary
        image_url = upload_image_to_cloudinary(image_file, image_file.name)
        if not image_url:
            raise serializers.ValidationError("Image upload failed.")
    
        # Save validated image URL to model field
        validated_data['Image'] = image_url
    
        return super().create(validated_data)