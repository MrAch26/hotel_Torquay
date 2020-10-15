from django.contrib import admin
from django.urls import path, include

from . import views
from .views import UserSignUp

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/signup/', UserSignUp.as_view(), name='signup'),
]