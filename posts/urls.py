from django import views
from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('post/<str:pk>', views.post, name = 'post'),   
]