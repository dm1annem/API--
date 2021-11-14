from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # rewiews = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 'rewiews'

    class Meta:
        model = User
        fields = ['id', 'username', ]