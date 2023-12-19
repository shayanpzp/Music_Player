from django.urls import path
from .views import sign_up, sign_in 

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('signin/', sign_in, name='sign_in'),
    
]