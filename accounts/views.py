from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import generic
from django.urls import reverse_lazy

#create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
