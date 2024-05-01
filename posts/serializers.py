from rest_framework.serializers import ModelSerializer
from . models import Post
from django.contrib.auth.models import User

# my serializers
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'body',
            'created_at'
        ]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]