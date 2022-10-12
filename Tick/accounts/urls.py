from django.urls import path, include
from . import views

app_name='accounts'

urlpatterns = [
    path('register',views.Register, name='signUp'),
    path('login', views.signin, name="login"),
    path("logout",views.user_logout, name="logout"),
]