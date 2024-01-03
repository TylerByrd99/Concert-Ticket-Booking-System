from django.shortcuts import render
from django.http import HttpResponse
from .models import Performance, Concert, User


# functions to connect to html pages
def base(request):
    return render(request, "base.html")


def home(request):
    return render(request, "base.html")


def login(request):
    return render(request, 'login.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def tickets(request):
    return render(request, 'tickets.html')


def find_shows(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        try:
            performance = Performance.objects.get(concert__artist=searched)
        except Performance.DoesNotExist:
            performance = None
        return render(request, 'find_shows.html', {'searched': searched, 'performance': performance})


def profile(request):
    login_list = User.objects.all()
    return render(request, 'profile.html', {'login_list': login_list})