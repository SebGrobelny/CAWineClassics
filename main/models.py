# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create models here
# Database models 
class Contact(models.Model):
    # __tablename__ = "contact"
    # id = models.Column(models.Integer, primary_key=True)
    name= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city =  models.CharField(max_length=200, default='')
    zipcode = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    single = models.CharField(max_length=200)
    multiple = models.CharField(max_length=200)
    looking = models.CharField(max_length=500)
    hear = models.CharField(max_length=500)
    time = models.DateTimeField(
         blank=True, null=True)

    #sumbission
    def submit(self):
        self.time = timezone.now()
        self.save()


    # def __repr__(self):
    #     return '<E-mail %r>' % self.email

# Create our database model
class Request(models.Model):
    # __tablename__ = "request"

    # id = models.Column(models.Integer, primary_key=True)
    name= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city =  models.CharField(max_length=200, default='')
    zipcode = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    single = models.CharField(max_length=200)
    multiple = models.CharField(max_length=200)
    looking = models.CharField(max_length=500)
    hear = models.CharField(max_length=500)
    requestedwine = models.TextField()
    time = models.DateTimeField(
         blank=True, null=True)

    #sumbission
    def submit(self):
        self.time = timezone.now()
        self.save()


    # def __repr__(self):
    #     return '<E-mail %r>' % self.email

class Inventory(models.Model):

	packaged = models.CharField(max_length=200)
	color = models.CharField(max_length=200)
	variety = models.CharField(max_length=200)
	lot = models.CharField(max_length=200)
	units = models.CharField(max_length=200)
	storage = models.CharField(max_length=200)
	year = models.CharField(max_length=200)
	ava = models.CharField(max_length=200)
	alc = models.CharField(max_length=200)
	chemanalysis = models.CharField(max_length=200)
	current = models.CharField(max_length=500)
	pending = models.CharField(max_length=500)
	other = models.CharField(max_length=500)
	promised = models.CharField(max_length=500)
	available = models.CharField(max_length=500)
	comments = models.CharField(max_length=500)

