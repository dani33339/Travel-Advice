from django.urls import path
from .views import (
    forumhome, detail, posts, create_post)

urlpatterns = [
    path("forumhome/", forumhome, name="forumhome"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),

]
