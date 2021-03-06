from django.urls import path
from .views import (
    UserRegisterView, UserEditView, PasswordsChangeView,
    ProfilePageView, EditProfilePageView, CreateProfilePageView)
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(
        template_name="registration/change-password.html"), name="password"),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name="profile_page"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_profile/', CreateProfilePageView.as_view(), name="create_profile"),
]
