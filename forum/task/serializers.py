from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Posts, Category, LikeDislike, Comments


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для CRUD категории"""
    class Meta:
        model = Category
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения постов"""
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = Posts
        exclude = ['published']


class CreatePostsSerializer(serializers.ModelSerializer):
    """Сериализатор для CRUD постов"""
    class Meta:
        model = Posts
        fields = '__all__'


class LikeDislikeSerializer(serializers.ModelSerializer):
    """Сериализатор для отображеня лайков и дизлайков"""
    user = UserSerializer()
    post = PostsSerializer()

    class Meta:
        model = LikeDislike
        fields = '__all__'


class CreateLikeDislikeSerializer(serializers.ModelSerializer):
    """Сериализатор для CRUD лайков и дизлайков"""
    class Meta:
        model = LikeDislike
        fields = '__all__'


class RecursiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'

        def recursive(self, value):
            serializer = self.parent.parent.__class__(value, context=self.context)
            return serializer.data


class CommentsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения комментов"""
    author_comment = UserSerializer()
    post = PostsSerializer()
    parent = RecursiveSerializer()

    class Meta:
        model = Comments
        fields = '__all__'


class CreateCommentsSerializer(serializers.ModelSerializer):
    """Сериализатор для CRUD комментов"""
    class Meta:
        model = Comments
        fields = '__all__'