from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "chatapp"
urlpatterns = [
    path('', TemplateView.as_view(template_name='chatapp/home.html'), name='home'),
]