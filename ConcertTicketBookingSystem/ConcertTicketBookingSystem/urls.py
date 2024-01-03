"""ConcertTicketBookingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from MyApps import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('base.html', views.home, name='home'),
    path('profile.html', views.profile, name='profile'),
    path('login.html', views.login, name='login'),
    path('find_shows.html', views.find_shows, name='find_shows'),
    path('sign_up.html', views.sign_up, name='sign_up'),
    path('tickets.html', views.tickets, name='tickets'),

]
