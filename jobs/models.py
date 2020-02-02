from django.db import models
from django.urls import reverse


class Job(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    experience = models.IntegerField(default=0)
    location = models.CharField(default='Bangalore', max_length=256)

    def get_absolute_url(self):
            return reverse('jobs:job_detail', kwargs={'pk': self.pk})
