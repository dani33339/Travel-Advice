from django.urls import path
from .views import (
    home, detail, posts,)

urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),

]
