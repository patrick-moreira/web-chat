from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "chatapp"
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('chat/', views.ChatView.as_view(), name='home'),
    path('message/', views.send_message, name='send_message'),
    path('load_messages/', views.load_messages, name='load_messages'),
    path('private/<int:user1>/<int:user2>', views.private_chat, name='private')
]