from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'terms_conditions']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Validating password and confirm password while registration
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password don't match")
        return data

    # Override the create method to handle password and password2
    def create(self, validated_data):
        # Remove password2 from the validated data
        validated_data.pop('password2')
        
        # Create the user with the remaining data
        user = User.objects.create_user(**validated_data)
        
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['email', 'password']
