from django.urls import path, include
from . import views


app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogOut, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verify, name="verify"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    path("update-password/", views.UpdatePasswordView.as_view(), name="password"),
    path("update-profile/", views.UpdateUserView.as_view(), name="update"),
    path("switch-hosting/", views.switch_hosting, name="switch-hosting"),
    path("<int:pk>/all-reservations/", views.all_reservations, name="all-reservations"),
]