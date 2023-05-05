from django.urls import path
from . import views



urlpatterns = [
    path('registrate/', views.registrate, name='registrate'),
    path('login_view/', views.login_view, name='login'),

]