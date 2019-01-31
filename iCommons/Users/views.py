# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth import login, authenticate

# Create your views here.


def Login(request):
    print(request.method)
    if request.method == 'GET':
        print("testing")
        context = {}
        return render(request, 'login.html', context)
    
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        print("user")
        login(request, user)

        return redirect(request,"../")


def view_account(request):
    context = {}
    return render(request, 'account.html', context)
