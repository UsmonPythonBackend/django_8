from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import UserBooks



def login_view(request):
    print(request.POST)
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/login.html',
                          context={"message": "Sorry, Password or Username incorrect, /n(try again) 🙁 "})
    return render(request, "auth/login.html")


def register_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return render(request, 'auth/register.html', context={"message_password": "Password error"})
        if User.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', context={"message": "User already exists"})
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return redirect('login')

    return render(request, "auth/register.html")


def logout_views(request):
    logout(request)
    return redirect('home')

@login_required()
def account_main_view(request):
    print(f"----------{request}")
    return render(request, 'account/main.html')


def account_about_view(request):
    print(f"----------{request}")
    return render(request, 'account/about.html')

def account_books_view(request, id):

    if request.method == "GET":
        user_id = request.GET["user"]
        active_books = UserBooks.objects.get(user__id=user_id)
        return render(request, 'account/active_books.html', {"active_books": active_books})