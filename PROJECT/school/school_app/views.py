from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


def logoutfrom(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return redirect('school_app:login')
  
def add(request):
    return render(request, 'home.html')
def dpart(request):
    return render(request, 'meeting-details.html')




def reg(request):
    if request.method == 'POST':
        uname = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username already taken')
                return redirect('school_app:reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('school_app:reg')
            else:
                user = User.objects.create_user(username=uname, email=email, password=password)
                user.save()
                return redirect('school_app:login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('school_app:reg')

    return render(request, 'register.html')



def log(request):
    if request.method =='POST': 
        username= request.POST['user']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('school_app:show_form')
          
        else:
            messages.info(request, "invalid credential")
            return redirect('school_app:login')

    return render(request, "login.html")


def show_form(request):
    return render(request, 'new.html')

from django.shortcuts import render


def show_form(request):
    if request.method == 'POST':
        # Process form data and handle submission
        # You can access the form data using request.POST dictionary
        # Perform any necessary validation or saving of data
        
        # Example: Get form data
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')
        
        # Perform any additional processing or saving of data
        
        # Example: Pass success message to template
        message = "Order Confirmed"
        
        context = {
            'message': message,
        }
        
        return render(request, 'confirmation.html', context)
    
    return render(request, 'new.html')
from django.shortcuts import render


def confirmation_view(request):
    return render(request, 'confirmation.html')
from django.shortcuts import redirect


def form_submission_view(request):
    return redirect('confirmation')













