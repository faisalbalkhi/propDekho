from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.hashers import make_password

from  properties_engine .models import  Property
from .models import User


def register(request):
    user_type = None
    if request.method == "POST":
        user_type = request.POST.get('user_type')
        username = request.POST.get('username')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if user_type == 'agent':
            user_type = True
        else:
            user_type = False
        encrypted_password = make_password(password2)
        if password1 == password2:
            user = User(user_type=user_type, username=username, mobile_number=mobile_number, email=email, password=encrypted_password)
            user.save()
            auth_login(request, user)
            if user.user_type:
                return redirect('dashboard_add_listing')
            return redirect('login')
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        # Get the username and password from the request.POST dictionary
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user with the provided username and password
        user = authenticate(request, username=username, password=password)
        print(user.user_type)

        if user is not None:
            # If authentication is successful, log the user in and redirect to home page
            auth_login(request, user)
            if user.user_type:
                return redirect('dashboard_add_listing')
            return redirect('index')
    else:
        # If the request method is GET, display the login form
        return render(request, 'index.html')
    

def logout_view(request):
    logout(request)
    return redirect('index')



def index(request):
    properties = Property.objects.all()
    print()
    print()
    print()
    print(properties)
    return render(request, 'index.html',{
        'properties': properties,
    })


def dashboard_add_listing(request):
    return render(request, 'dashboard-add-listing.html')


def contacts(request):
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


<<<<<<< HEAD
def pg_Guest(request):
    return render(request, 'pgGuest.html')


=======
def dashboard_agent(request):
    return render(request, 'dashboard-agents.html')


def dashboard_mypropfile(request):
    return render(request, 'dashboard-myprofile.html')


def agent_list(request):
    return render(request, 'agent-list.html')
>>>>>>> 19d5d10106b8bdc49faa0e02991229494e618b3b

