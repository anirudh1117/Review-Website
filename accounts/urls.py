from django.urls import path, include
from .views import register,login,logout,profile
from django.conf.urls import url

urlpatterns = [
    path('signup/', register, name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')), # <--social login
    path('profile/',profile,name='profile')
]