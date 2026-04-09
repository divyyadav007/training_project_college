from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def home(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'product.html')    

def about(request):
    return render(request, 'about.html')

def contact(request):
    data = Contact.objects.all()

    if request.method == "POST":
        # 1. Form se data nikalna
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # 2. Database mein save karna
        # Note: Check karein aapke models.py mein 'message' aur 'date' fields hain ya nahi
        c = Contact(
            name=name, 
            email=email, 
            phone=phone, 
            message=message, 
        )
        c.save()
        
        # Success flag bhejna
        return redirect('contact')
            
    # 3. GET request par saara data fetch karna
    
    return render(request, 'contact.html', {'data': data})

def signupView(request):

    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        userName = request.POST.get('userName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        user = User.objects.create_user(userName, email, password)
        user.first_name =  firstName
        user.last_name = lastName
        user.save()
        return redirect('/login')

    return render(request, 'signup.html')

def loginView(request):
    if request.method == "POST":
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        user = authenticate(request, username=userName, password=password)

        if user is not None:
            # 2. Start the session
            login(request, user)
            return redirect('/home') 
        else:
            # 3. Handle failed login
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')

    return render(request, 'login.html')
from django.shortcuts import render, redirect
from .models import Contact


def home(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'product.html')    

def about(request):
    return render(request, 'about.html')

def contact(request):
    data = Contact.objects.all()

    if request.method == "POST":
        # 1. Form se data nikalna
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # 2. Database mein save karna
        # Note: Check karein aapke models.py mein 'message' aur 'date' fields hain ya nahi
        c = Contact(
            name=name, 
            email=email, 
            phone=phone, 
            message=message, 
        )
        c.save()
        
        # Success flag bhejna
        return redirect('contact')
            
    # 3. GET request par saara data fetch karna
    
    return render(request, 'contact.html', {'data': data})