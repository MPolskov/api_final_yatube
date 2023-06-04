from rest_framework import routers
from django.urls import include, path

from .views import (
    PostViewSet,
    GroupViewSet,
    CommentViewSet,
    FollowViewSet
)


v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(r'^posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')
v1_router.register('follow', FollowViewSet,
                   basename='following')


urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
