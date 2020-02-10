from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Idea(models.Model):
    idea = models.TextField()
    save_time = models.TextField()
    save_money = models.TextField()
    save_effort = models.TextField()


    def get_absolute_url(self):
        return reverse('pragati:idea')