from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('Username already exists')


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CodeConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        username = data['username']
        code = data['code']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError('Пользователь не найден')

        if not hasattr(user, 'verification_code'):
            raise ValidationError('Код подтверждения не найден')

        if user.verification_code.code != code:
            raise ValidationError('Неверный код')

        return data
