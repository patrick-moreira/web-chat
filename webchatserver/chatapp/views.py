from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from .models import Message


class ChatView(generic.ListView):
    template_name = 'chatapp/home.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.all()


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('chatapp:login')
    template_name = 'registration/signup.html'


def send_message(request):

    dest = int(request.POST['to'])
    src = int(request.POST['from'])
    msg = request.POST['message']

    print(dest, src, msg)

    destUser = User.objects.get(id=dest)
    srcUser = User.objects.get(id=src)

    message = Message.objects.create(origin=srcUser, destination=destUser, text=msg, date=timezone.now())
    message.save()

    return redirect("chatapp:home")


def load_messages(request):

    dest = int(request.GET['to'])
    src = int(request.GET['from'])

    destUser = User.objects.get(id=dest)
    srcUser = User.objects.get(id=src)

    if dest == 1:
        messages = Message.objects.filter(destination=destUser)
    else:
        messages = Message.objects.filter(destination=destUser, origin=srcUser)

    return render_to_response('chatapp/messages.html', {'messages': messages})


# @login_required