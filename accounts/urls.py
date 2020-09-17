from django.urls import path
from .views import login,register,dashboard,logout

urlpatterns = [
    path('register',register,name="register"),
    path('login',login,name="login"),
    path('dashboard',dashboard,name="dashboard"),
    path('logout',logout,name='logout')
]