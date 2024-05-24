from django.urls import path
from users.views import *

app_name = 'users'
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LoogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile-edit/", ProfileEditView.as_view(), name="profile_edit")
]
