from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # Main/Home page (Jab koi sirf website.com khole)
    path('admin', admin.site.urls),
    path('', views.home, name='home'),
    
    # Baaki pages
    path('product', views.product, name='product'),
    path('about', views.about, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signupView, name='signup'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
]