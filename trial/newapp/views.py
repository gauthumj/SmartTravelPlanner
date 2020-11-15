from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, forms, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserInfo, User, UserTravel
import wikipedia
from .map import *
from .STPCode import *
# Create your views here.


def home(request):
    return render(request, 'newapp/dsa home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('newapp:main_page')
        else:
            messages.info(request, 'Username or password is incorrect')
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
                messages.info(request, 'username is already in use !')
                return redirect('newapp:signup')
            else:
                form.save()
                login(request, form)
                return redirect('newapp:main_page')

    else:
        form = UserInfo()

    return render(request, 'newapp/dsa signup.html', {'form': form})


@login_required(login_url='newapp:login_page')
def main_page(request):
    if request.method == "POST":
        text = str()
        global place_list
        text = request.POST.get('x')
        # print(text)
        place_list = text.split(',')
        # print(place_list)
        username = request.user.username
        if UserTravel.objects.filter(username=username).exists():
            temp = UserTravel.objects.get(username=username).places
            for i in place_list:
                temp = temp+i+','
            ut = UserTravel.objects.get(username=username)
            ut.places = temp
            ut.save()
        else:
            u = User.objects.get(username=username)
            temp = str()

            for i in place_list:
                temp += i+','
            ut = UserTravel(user=u, username=u.username, places=temp)
            ut.save()
        return redirect('newapp:display_page')

    return render(request, 'newapp/main_interface-test.html')


@login_required(login_url='newapp:login_page')
def display_page(request):
    final.clear()
    STACK.clear()
    # print(place_list)
    global stack
    route, stack = NextNode(place_list[0], place_list)
    # print(route)
    # print(stack)
    PlaceInfo=[wikipedia.page(x+' place').summary for x in stack[:len(stack)-1]]
    info = zip(stack,PlaceInfo)
    form = {
        'route': route,
        'info': info,
    }
    return render(request, 'newapp/dsa_path.html', context=form)


@login_required(login_url='newapp:login_page')
def map_display(request):
    get_map(stack)
    return render(request, 'newapp/display_map.html')


@login_required(login_url='newapp:login_page')
def profile_page(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(
                request, 'Your password was successfully updated !')
            return redirect('newapp:profile_page')
        else:
            messages.error(request, 'An error occured !')
            return redirect('newapp:profile_page')
    else:
        history = UserTravel.objects.get(username=request.user.username).places
        history = history[:len(history)-1]
        form = PasswordChangeForm(request.user)
        context = {
            'history': history,
            'form': PasswordChangeForm,
        }
    return render(request, 'newapp/dsa_profile.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('newapp:home')
