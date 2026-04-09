from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    # Main/Home page (Jab koi sirf website.com khole)
    path('home', views.home, name='home'),
    
    # Baaki pages
    path('product', views.product, name='product'),
    path('about', views.about, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signupView, name='signup'),
    path('login', views.loginView, name='login'),
=======
from . import views   # 👈 THIS IS REQUIRED

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('about/', views.about, name='aboutus'),
    path('contact/', views.contact, name='contact'),
>>>>>>> 90fc5028f2127f029afaa94a24d9818fd16d143c
]