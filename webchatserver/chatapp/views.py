from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return render(request, 'chatapp/index.html')


def public_chat(request):
    return render(request, 'chatapp/public_chat.html')


def login_view(request):
    nick = request.POST['name']
    passw = request.POST['password']

    if nick is None or passw is None:
        print("OLOCO")

    user = authenticate(request, username=nick, password=passw)

    if user is None:
        print("NAO LOGOU")
        return HttpResponse('Unauthorized', status=401)

    print(user)

    login(request, user)
    return redirect(request, 'chatapp/public_chat.html')
    # return redirect(render(request, 'chatapp/public_chat.html'))


def logout_view(request):
    logout(request)
    return redirect(render(request, 'chatapp/index.html'))


# @login_required