from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Added this for your login error handling

def home(request):
    return render(request, 'index.html')
@login_required
def product(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'product.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Create and save in one go
        Contact.objects.create(
            name=name, 
            email=email, 
            phone=phone, 
            message=message
        )
        messages.success(request, "Message sent successfully!")
        return redirect('contact')
            
    data = Contact.objects.all()
    return render(request, 'contact.html', {'data': data})

def signupView(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        userName = request.POST.get('userName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create user and set details
        user = User.objects.create_user(userName, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        return redirect('login') # Use URL name

    return render(request, 'signup.html')

def loginView(request):
    if request.method == "POST":
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        user = authenticate(request, username=userName, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') # Use URL name
        else:
            return render(request, 'login.html',{"error" :"Invalid username or password"} )

    return render(request, 'login.html')

def logoutView(request):
    logout(request) # Fixed typo 'reqeust'
    return redirect('home') # Better to redirect than render