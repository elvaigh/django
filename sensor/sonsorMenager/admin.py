# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Channel, Contact

admin.site.register(Channel)
admin.site.register(Contact)