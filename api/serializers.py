from rest_framework import serializers
from .models import DiveUser, Food
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.hashers import make_password
from django.conf import settings
from .nutritionix import Nutritionix


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = DiveUser
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}
        validators = [
            UniqueTogetherValidator(
                queryset=DiveUser.objects.all(),
                fields=['email']
            )
        ]

    def create(self, validated_data):
        user = DiveUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            level='user'
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.password = make_password(password)
        return super().update(instance, validated_data)


class FoodSerializer(serializers.ModelSerializer):
    calories = serializers.IntegerField(required=False)

    class Meta:
        model = Food
        fields = ['id', 'name', 'date', 'time', 'calories', 'note']

    def create(self, validated_data):
        if not validated_data.get('calories'):
            nutritionix = Nutritionix(settings.NUTRINIX_APP_ID, settings.NUTRINIX_APP_KEY)
            validated_data['calories'] = nutritionix.get_calories(validated_data['name'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if not validated_data.get('calories'):
            nutritionix = Nutritionix(settings.NUTRINIX_APP_ID, settings.NUTRINIX_APP_KEY)
            validated_data['calories'] = nutritionix.get_calories(validated_data['name'])
            print(validated_data)
        return super().update(instance, validated_data)
