from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import Group
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ["username", "url", "groups"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={
            "input_type": "password",
        },
        write_only=True,
    )
    user_role = serializers.ChoiceField(
        choices=[
            "accountant",
            "dispatcher",
            "driver",
        ],
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
            "user_role",
        ]
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def save(self):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        user_role = self.validated_data["user_role"]
        if password != password2:
            raise serializers.ValidationError({"Error": "Pasword didn't match!"})

        if not user_role:
            raise serializers.ValidationError({"Error": "Please enter user role"})

        if User.objects.filter(username=self.validated_data["username"]).exists():
            raise serializers.ValidationError({"error": "username already exists!"})
        group = Group.objects.get(name=str(user_role))
        account = User(
            username=self.validated_data["username"],
        )
        account.set_password(password)
        account.save()
        group.user_set.add(account)

        return account
