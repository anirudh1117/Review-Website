from django.urls import path
from .views import register,login,logout

urlpatterns = [
    path('signup/', register, name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout')
]