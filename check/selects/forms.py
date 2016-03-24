from django.forms import ModelForm
from selects.models import Continent,Country,Location

class ContinentForm(ModelForm):
	class Meta:
		model = Continent
		fields = ['name']

class CountryForm(ModelForm):
	class Meta:
		model = Country
		fields = ['name','continent']

class LocationForm(ModelForm):
	class Meta:
		model = Location
		fields = ['continent','country'] 