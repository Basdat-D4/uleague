from django.urls import path
from authentication.views import login_user, logout_user, register_user

app_name = 'authentication'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register_user, name='register_user'),
]