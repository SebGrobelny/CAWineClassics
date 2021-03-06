# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect

from .models import Inventory,Contact

from .forms import ContactForm
from .forms import RequestForm

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
			contact = form.save(commit=False)

			time = str(datetime.now(timezone('US/Pacific')))
			time = time.split(".")[0]
			contact.time = time




			contact.save()
			# return redirect('home')
			return HttpResponseRedirect("https://californiawineclassics.com/home")
    #otherwise render form 
	else:
		form = ContactForm()
	
	return render(request,'main/contact.html', {'form': form})

def search(request):

	#check to see if method is get
	if request.method == "GET":

		variety = request.GET.get('variety')
		print variety
		AVA = request.GET.get('AVA')
		print AVA
		year = request.GET.get('year')
		print year
		form = RequestForm()

		#overcoming the return None in some cases

		if variety:
			foundwine = Inventory.objects.filter(variety__icontains=variety)

			if AVA:
				foundwine = foundwine.filter(ava__icontains=AVA)

			if year:
				foundwine = foundwine.filter(year__icontains=year)

		elif AVA:
			foundwine = Inventory.objects.filter(ava__icontains=AVA)

			if year:
				foundwine = foundwine.filter(year__icontains=year)
		#both AVA and variety are none
		else:
			foundwine = None

	elif request.method == "POST":
		form = RequestForm(request.POST)

		if form.is_valid():

			requestedwine = request.POST.getlist('check')
			for wine in requestedwine:
				print wine
				form = RequestForm(request.POST)
				inventory = Inventory.objects.filter(lot=wine)

				requested  = form.save(commit=False)
				requested.requestedwine= str(inventory[0].variety)+" , "+str(inventory[0].lot)

				time = str(datetime.now(timezone('US/Pacific')))
				time = time.split(".")[0]
				requested.time = time

				requested.save()


			# return redirect('home')
			return HttpResponseRedirect("https://californiawineclassics.com/home")

	else:
		foundwine = None
		form = RequestForm()

	return render(request, 'main/search.html', {'foundwine':foundwine, 'form':form})


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
	if request.method == "POST":
		form = RequestForm(request.POST)

		if form.is_valid():


			requestedwine = request.POST.getlist('check')
			for wine in requestedwine:
				print wine
				form = RequestForm(request.POST)
				inventory = Inventory.objects.filter(lot=wine)

				requested  = form.save(commit=False)
				requested.requestedwine= str(inventory[0].variety)+" , "+str(inventory[0].lot)

				time = str(datetime.now(timezone('US/Pacific')))
				time = time.split(".")[0]
				requested.time = time

				requested.save()


			# return redirect('home')
			return HttpResponseRedirect("https://californiawineclassics.com/home")

	else:
		reds = Inventory.objects.filter(color='Red')
		whites = Inventory.objects.filter(color='White')
		form = RequestForm()

	return render(request, 'main/stillwine.html', { 'reds': reds, 'whites': whites, 'form': form})
