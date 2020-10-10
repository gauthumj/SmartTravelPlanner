from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth import login,authenticate,logout,forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserInfo,User,UserTravelForm,UserTravel
from django.http import HttpResponse,Http404
import json
# Create your views here.


def home(request):
    return render(request, 'newapp/dsa home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('newapp:main_page')
        else:
            messages.info(request,'Username or password is incorrect')
            return redirect('newapp:login_page')

    else:
        return render(request, 'newapp/login.html')



def signup(request):
    if request.method == "POST":
        form = UserInfo(request.POST)
        if form.is_valid():
            # username = request.POST.get('username')
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists:
                messages.info(request,'username is already in use !')
                return redirect('newapp:signup')
            else:
                form.save()
                login(request,form)
                return redirect('newapp:main_page')

    else:
        form = UserInfo()

    return render(request, 'newapp/dsa signup.html', {'form': form})

@login_required(login_url='newapp:login_page')
def main_page(request):
    if request.method == "POST":
        form = UserTravelForm(request.POST)
        if form.is_valid():
            place_list = request.POST.getlist('places[]')
            username = request.user.username
            if UserTravel.objects.filter(username=username).exits():
                temp = UserTravel.objects.get(username=username).places
                for i in place_list:
                    temp = temp+','+i
                ut = UserTravel.objects.get(username=username)
                ut.places = temp
                ut.save()
            else:
                u = User.objects.get(username=username)
                for i in place_list:
                    temp = temp+','+i
                ut = UserTravel(u.id,username=u.username,places=temp)
                ut.save()
    else:
        form = UserTravelForm()

    return render(request,'newapp/main-interface.html',{'form' : form})

def logout_user(request):
    logout(request)
    return redirect('newapp:home')
