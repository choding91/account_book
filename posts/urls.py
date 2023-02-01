from django.urls import path
from posts.views import PostView


urlpatterns = [
    path("post/", PostView.as_view(), name="post_view"),
]
