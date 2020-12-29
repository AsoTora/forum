from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # path('auth/logout', Logout.as_view()),

    path('posts/list/', PostsListView.as_view()),
    path('posts/create/', PostsCreateView.as_view()),
    path('posts/retrieve/<int:pk>/', PostsRetrieveView.as_view()),
    path('posts/update/<int:pk>/', PostsUpdateView.as_view()),
    path('posts/destroy/<int:pk>/', PostsDestroyView.as_view()),

    path('category/list/', CategoryListView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/retrieve/<int:pk>/', CategoryRetrieveView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view()),
    path('category/destroy/<int:pk>/', CategoryDestroyView.as_view()),

    path('comments/all/', CommentsListView.as_view()),
    path('comments/create/', CommentsCreateView.as_view()),
    path('comments/retrieve/<int:pk>/', CommentsRetrieveView.as_view()),
    path('comments/update/<int:pk>/', CommentsUpdateView.as_view()),
    path('comments/destroy/<int:pk>/', CommentsDestroyView.as_view()),

    path('like/create/', LikeDislikeCreateView.as_view()),
    path('like/all/', LikeDislikeListView.as_view()),

]