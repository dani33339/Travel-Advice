from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.guideProfile,name= "guide-profile"),
    path('account/',views.userAccount, name="account"),
    path('edit-account/',views.editAccount, name="edit-account"),
]