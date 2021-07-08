from django.contrib.auth import get_user_model

from rest_auth.models import TokenModel

from rest_framework import serializers

from .models import Users, Moderators


class UsersRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    photo = serializers.ImageField()

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        user = Users.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            photo=validated_data.get('photo'),
            phone=validated_data.get('phone'),
            email=validated_data.get('email'),
        )
        return user


class ModeratorsRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        user = Moderators.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        return user


class UsersLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ModeratorsLoginSerializer(UsersLoginSerializer):
    pass
