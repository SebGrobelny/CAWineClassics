# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Inventory,Contact

from .forms import ContactForm

from datetime import datetime
from pytz import timezone

# Create your views here.

#standard views (Don't interact with DBs)
def splash(request):
	return render(request,'main/splash.html')

def home(request):
	return render(request,'main/home.html')

def about(request):
	return render(request,'main/about.html')

def team(request):
	return render(request,'main/team.html')

def katie(request):
	return render(request,'main/katie.html')

def leslie(request):
	return render(request,'main/leslie.html')

def business(request):
	return render(request,'main/business.html')

def contact(request):
	#check to see if method is post
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			# contact = Contact()
			print request
			contact = form.save(commit=False)

			time = str(datetime.now(timezone('US/Pacific')))
			time = time.split(".")[0]
			contact.time = time




			contact.save()
			return redirect('splash', pk=contact.pk)
    #otherwise render form 
	else:
		form = ContactForm()
	
	return render(request,'main/contact.html', {'form': form})

def winery(request):
	return render(request,'main/winery.html')

def ice_house(request):
	return render(request,'main/ice_house.html')

def purchase(request):
	return render(request,'main/purchase.html')

def sparkling(request):
	return render(request,'main/sparkling.html')

def serendipity(request):
	return render(request,'main/serendipity.html')

def champenoise(request):
	return render(request,'main/champenoise.html')

def news(request):
	return render(request, 'main/news.html')

def event(request):
	return render(request, 'main/event.html')

#view that interacts with DB
def still_wine(request):
	#use  QuerySet to obtain the desired filters
	reds = Inventory.objects.filter(color='Red')
	whites = Inventory.objects.filter(color='White')

	return render(request, 'main/stillwine.html', { 'reds': reds, 'whites': whites})
