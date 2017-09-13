# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from users.models import User

from django.contrib import admin

# Register your models here.

class UsersAdmin (admin.ModelAdmin):
    list_display    = ['first_name', 'last_name', 'username', 'password', 'address', 'sex', 'phone']
    list_filter     = ['sex']
    search_filter   = []
    list_per_page   = 25

admin.site.register(User, UsersAdmin)
