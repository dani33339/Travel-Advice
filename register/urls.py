from django.urls import path
from .views import signup,signin,update_profile, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("update_profile/", update_profile, name="update_profile"),
    path("logout/", logout, name="logout"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="register/password_reset.html"), name="reset_password"), #(template_name="register/password_reset.html")
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="register/password_reset_sent.html"),name="password_reset_done"), #(template_name="register/password_reset_sent.html")
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="register/password_reset_form.html"),name="password_reset_confirm"),#(template_name="register/password_reset_form.html")
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="register/password_reset_done.html"),  name="password_reset_complete"),#(template_name="register/password_reset_done.html")
]