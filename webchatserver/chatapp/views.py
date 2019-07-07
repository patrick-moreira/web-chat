from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render_to_response
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


@login_required
def send_message(request):

    dest = request.POST.get('to')
    if dest == "global":
        dest = None
    else:
        dest = int(dest)

    src = int(request.POST.get('from'))
    msg = request.POST.get('message')

    src_user = User.objects.get(id=src)

    if dest is None:
        message = Message.objects.create(origin=src_user, text=msg, date=timezone.now())

    else:
        dest_user = User.objects.get(id=dest)
        message = Message.objects.create(origin=src_user, destination=dest_user, text=msg, date=timezone.now())

    print(dest, src, msg)

    message.save()

    return redirect("chatapp:home")


def private_chat(request, user1, user2):
    return render_to_response('chatapp/private.html', {"src": user1, "dest": user2, "user": request.user})


@login_required
def load_messages(request):

    dest = request.GET.get('to')
    if dest == "global":
        dest = None
    else:
        dest = int(dest)

    src = int(request.GET.get('from'))

    src_user = User.objects.get(id=src)

    if dest is None:
        messages = Message.objects.filter(destination=None)
    else:
        dest_user = User.objects.get(id=dest)
        print("Getting messages between " + str(src_user.username) + " and " + str(dest_user.username))
        messages = Message.objects.filter(
            Q(destination=dest_user, origin=src_user) | Q(destination=src_user, origin=dest_user)).order_by('date')

    return render_to_response('chatapp/messages.html', {'messages': messages, "user": request.user})
