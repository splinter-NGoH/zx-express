from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import Group
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields = ('id','name')


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ["username",  "url", "groups"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }
