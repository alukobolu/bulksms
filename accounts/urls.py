from django.urls import path, include
from . import views

app_name = "accounts_api"

urlpatterns = [
    path('welcome', views.welcome_email_view, name='welcome'),
    path('user/', views.user_view.as_view(), name='get_user'),                       #Check user api
    path('register', views.register_view.as_view(), name='register_user'),              #Register User
    path('login', views.login_view.as_view(), name='login_user'),                       #API login validator

    # path('auth/', include('dj_rest_auth.urls')),
    path('check_user/<user>', views.check_user.as_view(), name='check_user'),
    path('verify/email/',  views.verify_email.as_view(), name='verify_email'),               #verify email with otp
    path('set_password', views.setting_password, name='set_password'),

    # URLs that do not require user to be logged in djrest auth.
    # ---------------------------------------------------------------------------
    # login/                  Login Url
    # password/reset/         Reset password
    # password-reset/confirm/<uidb64>/<token>/        Reset password link
    
    # URLs that require a user to be logged in djrest auth.
    # -----------------------------------------------------------------------
    # logout/                 Logout url
    # user/                   Check the user who is logged in
    # password/change/        Change the logged in user password
    # token/verify/           verify token
    # token/refresh/          Refresh the jwt token
]