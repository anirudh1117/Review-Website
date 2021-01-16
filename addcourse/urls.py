from django.urls import path
from .views import addcourse


urlpatterns = [  
    path('', addcourse, name='courseadd'),

]