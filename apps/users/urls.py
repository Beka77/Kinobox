from django.urls import path
from apps.users.views import register, user_login, account, account_update
from django.contrib.auth import views as auth_views  # import this
from django.contrib.auth.views import LogoutView
from apps.settings.views import register_error, user_not_found

urlpatterns = [
    path("register/", register, name="register"),
    path("register/error/", register_error, name="register_error"),
    path("user_login/", user_login, name="user_login"),
    path("user/not_found/", user_not_found, name="user_not_found"),
    path("setting/user/<str:username>", account_update, name="account_update"),
    path("account/<str:username>", account, name="account"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
]
