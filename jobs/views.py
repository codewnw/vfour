from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from jobs.models import (Job)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class JobList(ListView):
    model = Job


class JobDetailView(PermissionRequiredMixin, DetailView):
    model = Job
    permission_required = ('jobs.view_job')

class CreateJobView(PermissionRequiredMixin, CreateView):
    model = Job
    fields = ('title', 'description', 'experience', 'location')
    permission_required = ('jobs.add_job')


class UpdateJobView(PermissionRequiredMixin, UpdateView):
    model = Job
    fields = ('title', 'description', 'experience', 'location')
    permission_required = ('jobs.change_job')


class DeleteJobView(PermissionRequiredMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('jobs:all')
    permission_required = ('jobs.delete_job')
