from django.urls import path
from .views import register,login

urlpatterns = [
    path('signup/', register, name='signup'),
    path('login/',login,name='login'),
]