from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

import csv
from .models import Book, File
import pandas as pd

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.

fs = FileSystemStorage(location='tmp')

@login_required(login_url='login')
def Home(request):
    return render(request, 'home.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get("pass")
        
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home/')
        else:
            return HttpResponse("Username or Password is incorrect")
    else:    
        return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            return HttpResponse("Password does not match")
        
        else:
        
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
       
        
        
    return render(request, 'signup.html')

@login_required(login_url='login')
@csrf_exempt
def get_data(request):
    response = Book.objects.all()
    return render(request,'data.html', {'response': response})
    

@login_required(login_url='login')
@csrf_exempt
def upload_data(request):
    if request.method == "POST":
        file = request.FILES['file']
        obj = File.objects.create(file=file)
        create_db(obj.file)
    return render(request,'upload.html')
    
def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    print(df.values)
    list_of_csv = [list(row) for row in df.values ]
    
    for l in list_of_csv:
        Book.objects.create(
            title = l[1],
            author = l[2],
            authors = l[3],
            isbn13 = l[4],
            isbn10 = l[5],
            price = l[6],
            publisher = l[7],
            pubyear = l[8],
            subjects = l[9],
            pages = l[10],
        ) 
    print(df)
    

    