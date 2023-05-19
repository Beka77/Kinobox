from django import forms
from django.shortcuts import render, redirect
from apps.settings.models import Settings
from .models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# from apps.users.forms import RegisterUserForm
# Create your views here.

# def register(request):
#     setting = Settings.objects.latest('id')
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         if password == confirm_password:
#             if username and email and password and confirm_password:
#                 try:
#                     user = User.objects.create(username = username, email = email)
#                     user.set_password(password)
#                     user.save()
#                     user = User.objects.get(username = username)
#                     user = authenticate(username = username, password = password)
#                     login(request, user)
#                     return redirect('index')
#                 except:
#                     return redirect('register_error')
#             else:
#                 return redirect('register_error')
#         else:
#             return redirect('register_error')
#     context = {
#         'setting' : setting,
#     }
#     return render(request, 'register.html', context)


def register(request):
    setting = Settings.objects.latest("id")
    context = {
        "setting": setting,
    }
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect("login")
    return render(request, "register.html", context)


# def login(request):
#     setting = Settings.objects.latest('id')
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             user = User.objects.get(username = username)
#             user = authenticate(username = username, password = password)
#             login(request, user)
#             return redirect('index')
#         except:
#             return redirect('user_not_found')
#     context = {
#         'setting' : setting,
#     }
#     return render(request, 'login.html', context)


def user_login(request):
    setting = Settings.objects.latest("id")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
        except:
            return redirect("user_not_found")
    context = {
        "setting": setting,
    }
    return render(request, "login.html", context)


def account(request, username):
    setting = Settings.objects.all()
    user = User.objects.get(username=username)
    context = {
        "user": user,
        "setting": setting,
    }
    return render(request, "account.html", context)


def account_update(request, username):
    user = User.objects.get(username=username)
    setting = Settings.objects.latest("id")
    if request.method == "POST":
        if "update" in request.POST:
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            user = User.objects.get(username=username)
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone = phone
            user.save()
            return redirect("account", user.username)
        if "delete" in request.POST:
            user = User.objects.get(username=username)
            user.delete()
            return redirect("index")
        if "update_password" in request.POST:
            password = request.POST.get("password")
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")
            if new_password == confirm_password:
                try:
                    user = User.objects.get(username=request.user.username)
                    if user.check_password(password):
                        user.set_password(new_password)
                        user.save()
                        return redirect("index", user.username)
                    else:
                        return HttpResponse("Текущий пароль не верный")
                except:
                    return HttpResponse("Пользователь не найден")
            else:
                return HttpResponse("Пароли различаются")
    context = {
        "user": user,
        "setting": setting,
    }
    return render(request, "account_update.html", context)
