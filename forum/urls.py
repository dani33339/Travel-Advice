from django.urls import path
from .views import (
    forumhome, detail, posts, create_post, latest_posts, search_result)

urlpatterns = [
    path('', forumhome, name="forumhome"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("search", search_result, name="search_result"),

]
