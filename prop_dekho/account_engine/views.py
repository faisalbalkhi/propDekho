from django.shortcuts import render


def register(request):
    if request.method == "POST":
        individual = request.POST.get('individual')
        agent = request.POST.get('agent')
        username = request.POST.get('username')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(individual)
        print(username)

def index(request):
    return render(request, 'index.html')


def dashboard_add_listing(request):
    
    return render(request, 'dashboard-add-listing.html')