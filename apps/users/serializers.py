from django.contrib.auth import authenticate

from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            'email',
            "first_name",
            "last_name",
            "password",
            "repeat_password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("repeat_password"):
            raise serializers.ValidationError("Passwords don't match.", code='password')

        if not attrs.get('first_name') or not attrs.get("last_name"):
            raise serializers.ValidationError('first name and last name cannot be empty.')

        if not attrs.get('email'):
            raise serializers.ValidationError('email must be set')

        return attrs

    def create(self, validated_data):
        validated_data.pop("repeat_password")
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        username_or_email = attrs.get('username_or_email')
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get('request'),
            username=username_or_email,
            password=password
        )
        if user is None:
            user = User.objects.filter(email=username_or_email).first()
            if user:
                user = authenticate(
                    request=self.context.get('request'),
                    username=user.username,
                    password=password
                )

        if not user:
            msg = 'Unable to log in with provided credentials.'
            raise serializers.ValidationError(msg, code='authorization')

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return {
            'refresh': str(refresh),
            'access': str(access)
        }
