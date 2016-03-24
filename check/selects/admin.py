from django.contrib import admin

# Register your models here.
from selects.models import Continent
admin.site.register(Continent)

from selects.models import Country
admin.site.register(Country)

from selects.models import Location
admin.site.register(Location)

