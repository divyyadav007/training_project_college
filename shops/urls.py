from django.urls import path
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
]