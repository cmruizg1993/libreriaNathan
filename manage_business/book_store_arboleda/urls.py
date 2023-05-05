from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.loginPage,name='login'),
    path('viewcart/', views.viewcart,name='viewcart'),
    path('addbook/', views.addbook,name='addbook'),
    path('register/', views.registerPage,name='register'),
    path('logout/', views.logoutPage,name='logout'),
    path('addtocart/<str:pk>', views.addtocart,name='addtocart'),
    path('deleteBook/<str:pk>', views.deleteBook,name='deleteBook'),
    path('updateBook/<str:pk>', views.updateBook,name='updateBook'),
    path('removeBookFromCart/<str:book_id>', views.removeBookFromCart,name='removeBookCustomer'),
]