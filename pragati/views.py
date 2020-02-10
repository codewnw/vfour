from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DeleteView, CreateView, DetailView )
from .models import Idea

# Create your views here.

class HomeView(TemplateView):
    template_name = 'pragati/home.html'


class IdeaListView(ListView):
    model = Idea

class IdeaCreateView(CreateView):
    model = Idea
    template_name = 'pragati/idea_form.html'
    fields = ['idea', 'save_time', 'save_money', 'save_effort']

class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'pragati/idea_detail.html'


