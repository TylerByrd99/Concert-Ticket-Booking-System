from django.contrib import admin

# Register your models here.
from MyApps.models import Concert

admin.site.register(Concert)

from MyApps.models import Ticket

admin.site.register(Ticket)

from MyApps.models import Venue

admin.site.register(Venue)

from MyApps.models import Performance

admin.site.register(Performance)
