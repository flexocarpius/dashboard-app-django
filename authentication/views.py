# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.models import Category, Task, Employee
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                # Create categories and tasks
                bugs = Category(title='Bugs', icon='bug_report')
                bugs.save()
                website = Category(title='Website', icon='code')
                website.save()
                server = Category(title='Server', icon='cloud')
                server.save()

                Task(content='Sign contract for "What are conference organizers afraid of?"', state=True, category=bugs).save()
                Task(content='Lines From Great Russian Literature? Or E-mails From My Boss?', state=True, category=bugs).save()
                Task(content='Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit', state=True, category=bugs).save()
                Task(content='Create 4 Invisible User Experiences you Never Knew About', state=True, category=bugs).save()
                
                Task(content='Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit', state=True, category=website).save()
                Task(content='Sign contract for "What are conference organizers afraid of?"', state=True, category=website).save()
                
                Task(content='Lines From Great Russian Literature? Or E-mails From My Boss?', state=True, category=server).save()
                Task(content='Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit', state=True, category=server).save()
                Task(content='Create 4 Invisible User Experiences you Never Knew About', state=True, category=server).save()

                Employee(name='Dakota Rice', country='Niger', city='Oud-Turnhout', salary=36738).save()
                Employee(name='Minerva Hooper', country='Curaçao', city='Sinaai-Waas', salary=23789).save()
                Employee(name='Sage Rodriguez', country='Netherlands', city='Baileux', salary=56142).save()
                Employee(name='Philip Chaney', country='Korea, South', city='Overland Park', salary=38735).save()
                Employee(name='Doris Greene', country='Malawi', city='Feldkirchen in Kärnten', salary=63542).save()
                Employee(name='Mason Porter', country='Chile', city='Gloucester', salary=78615).save()
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def logout_user(request):
    # Clean all database.
    Category.objects.all().delete()
    Task.objects.all().delete()
    Employee.objects.all().delete()
    logout(request)
    return redirect("/login/")

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
