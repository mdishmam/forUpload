from django.urls import path
from . import views

urlpatterns = [
    #path('', views.WrittingSpace, name='homepage'),
    path('', views.WrittingSpace, name = 'contentcreation'),
    path('register/', views.Register, name = 'registerpage'),
    path('login/', views.LoginPage, name = 'loginpage'),
    path('logout/', views.LogoutUser, name = 'logoutpage'),
    path('test/', views.testView, name = 'test'),
    #path('auth/', views.fbAuthenticate, name = 'fbPageAuth'),

]