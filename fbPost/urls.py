from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.fbAuthenticate, name = 'fbPageAuth'),
    #path('auth/after', views.postAuth, name = 'afterAuth'),
    path('login/device-based/regular/login/', views.postAuth, name = 'afterAuth'),
]