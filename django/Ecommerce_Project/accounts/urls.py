from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('signup/', views.signUpView, name='signup'),
    path('logout/', views.logoutView, name='logout'),
]