from rest_framework import serializers
from .models import DiveUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiveUser
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = DiveUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            level='user'
        )
        return user
