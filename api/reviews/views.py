from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Review


# пользователи размещавшие информацию об отзывах:
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer



# =========== Отзывы =========
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer


