from ast import Sub
from email import message
from django.shortcuts import render
from core.forms import ContactForm
from core.models import Contact
from django.http import HttpResponseRedirect
from django.views import View
from django import forms
# Create your views here.
def success(request):
  return render(request,'core/success.html')
def home(request):
  context = {'home': 'active'}
  return render(request, 'core/home.html', context)

# def contact(request):
#   context = {'contact': 'active'}
#   return render(request, 'core/contact.html', context)

def contact(request):
	form=ContactForm()
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return success(request)
	
	return render(request ,'core/contact.html',{'form':form})
