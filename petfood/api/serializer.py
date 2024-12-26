from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

# class UserRegisterSerializer(serializers.ModelSerializer):
#     password1 = serializers.CharField(write_only=True, required=False)
#     password2 = serializers.CharField(write_only=True, required=False)

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         # Dynamically set 'password1' and 'password2' as required only for POST requests
#         request = kwargs.get('context', {}).get('request', None)
#         if request and request.method == 'POST':
#             self.fields['password1'].required = True
#             self.fields['password2'].required = True
        

#     def validate(self, data):
#         # Check if password1 and password2 exist in the data
#         if 'password1' in data and 'password2' in data:
#             # Ensure password1 and password2 match
#             if data['password1'] != data['password2']:
#                 raise serializers.ValidationError("Passwords do not match.")
#         return data

#     def create(self, validated_data):
#         # Hash the password
#         password = validated_data.pop('password1')  # Use password1 and remove from validated_data
#         validated_data['password'] = make_password(password)  # Store hashed password
#         validated_data.pop('password2', None)  # Remove password2, no longer needed
#         return super().create(validated_data)

