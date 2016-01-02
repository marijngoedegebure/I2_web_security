from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView


class CreateUserView(CreateView):
    template_name = 'safe/create_user_template.html'
    form_class = UserCreationForm
