# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required
def home(request):
	return render(request,"admin/index.html")