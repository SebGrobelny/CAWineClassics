# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Request
from .models import Contact
from .models import Inventory

# Register your models here.
admin.site.register(Request)

admin.site.register(Contact)

admin.site.register(Inventory)



