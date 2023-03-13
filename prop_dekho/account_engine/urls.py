from django.urls import path
from account_engine import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
]