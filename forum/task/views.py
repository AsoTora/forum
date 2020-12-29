from rest_framework import generics, permissions, status, pagination
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import *


class Logout(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class Pagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 1000


class PostsListView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsRetrieveView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsCreateView(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = CreatePostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostsUpdateView(generics.UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]


class PostsDestroyView(generics.DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryDestroyView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CommentsListView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentsRetrieveView(generics.RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentsCreateView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CreateCommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentsUpdateView(generics.UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentsDestroyView(generics.DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LikeDislikeCreateView(generics.CreateAPIView):
    queryset = LikeDislike.objects.all()
    serializer_class = CreateLikeDislikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LikeDislikeListView(generics.ListAPIView):
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer