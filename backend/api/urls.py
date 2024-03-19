from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('signin/', views.SigninView.as_view(), name='signin'),
]
