from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.guideProfile,name= "guide-profile"),
    path('account/',views.userAccount, name="account"),
    path('edit-account/',views.editAccount, name="edit-account"),
    path('create-skill/', views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),
]