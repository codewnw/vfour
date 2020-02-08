from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from jobs.models import Job


class Command(BaseCommand):
    help = 'Creates groups and permission'

    def handle(self, *args, **options):
        hr, created = Group.objects.get_or_create(name='HR')
        candidate, created = Group.objects.get_or_create(name='Candidate')

        job = ContentType.objects.get_for_model(Job)

        can_add_job = Permission.objects.get(
            codename='add_job', name='Can add job', content_type=job)
        can_change_job = Permission.objects.get(
            codename='change_job', name='Can change job', content_type=job)
        can_delete_job = Permission.objects.get(
            codename='delete_job', name='Can delete job', content_type=job)
        can_view_job = Permission.objects.get(
            codename='view_job', name='Can view job', content_type=job)

        candidate.permissions.add(can_view_job)
        hr.permissions.add(can_add_job, can_change_job,
                           can_delete_job, can_view_job)
