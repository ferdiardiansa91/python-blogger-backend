# Created by Ferdi Ardiansa
# Copyright. All rights reserved

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

class User(models.Model):
    TYPE_GENDER = (
        ('M', 'Males'),
        ('F', 'Females'),
    )

    first_name      = models.CharField(max_length = 255)
    last_name       = models.CharField(max_length = 255)
    username        = models.CharField(max_length = 255)
    email           = models.CharField(max_length = 50)
    sex             = models.CharField(max_length = 1, choices = TYPE_GENDER)
    phone           = models.CharField(max_length = 15, blank = True)
    password        = models.CharField(max_length = 255)
    address         = models.TextField(blank = True)

    def __unicode__(self):
        return self.username
