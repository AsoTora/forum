from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Posts, Category, LikeDislike, Comments, Statistics


class RecursiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'

        def recursive(self, value):
            serializer = self.parent.parent.__class__(value, context=self.context)
            return serializer.data


class CreateCommentsSerializer(serializers.ModelSerializer):
    """Comments CRUD"""
    class Meta:
        model = Comments
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    """Statistic"""
    class Meta:
        model = Statistics
        fields = ['calculate_stat', ]

class UserSerializer(serializers.ModelSerializer):
    """User information"""
    class Meta:
        model = User
        fields = ['username', 'password']


class CategorySerializer(serializers.ModelSerializer):
    """Categories CRUD"""
    class Meta:
        model = Category
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    """Posts information"""
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = Posts
        exclude = ['published']


class CreatePostsSerializer(serializers.ModelSerializer):
    """Posts CRUD"""
    class Meta:
        model = Posts
        fields = '__all__'


class LikeDislikeSerializer(serializers.ModelSerializer):
    """Likes and dislikes"""

    class Meta:
        model = LikeDislike
        fields = ['like_or_dislike', ]

class CommentsSerializer(serializers.ModelSerializer):
    """Comments view"""
    author_comment = UserSerializer()
    post = PostsSerializer()
    parent = RecursiveSerializer()

    class Meta:
        model = Comments
        fields = '__all__'