from django.urls import path
from posts.views import PostDetailView, PostView


urlpatterns = [
    path("post/", PostView.as_view(), name="post_view"),
    path("post/<int:post_id>/", PostDetailView.as_view(), name="post_detail_view"),
]
