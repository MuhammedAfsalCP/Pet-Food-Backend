from rest_framework import serializers
from .models import User,Products
from django.contrib.auth.hashers import make_password

class UserRegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField( required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')
    
    def save(self):

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"Error": "Password Does Not Match"})

        

        account = User(
            email=self.validated_data["email"], 
            username=self.validated_data["username"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"]
        )
        account.set_password(password)
        account.save()

        return account


class ProductsSeriealizer(serializers.ModelSerializer):

    class Meta:
        model=Products
        fields='__all__'
