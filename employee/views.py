from django.shortcuts import render
from django.views.generic import (TemplateView, DeleteView, ListView)
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Profile

# Create your views here.
class ProfileView(LoginRequiredMixin, TemplateView):
    model = Profile
    template_name = 'employee/profile.html'
    login_url = '/accounts/login/'