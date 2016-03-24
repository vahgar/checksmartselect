from django.shortcuts import render, HttpResponse
from selects.forms import ContinentForm,CountryForm,LocationForm
# Create your views here.
def checkselect(request):
	form_x = LocationForm();
	context = {'form':form_x}
	return render(request,'result.html',context);
