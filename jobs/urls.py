from django.conf.urls import url
from . import views

app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.JobList.as_view(), name='all'),
    url(r'^list$', views.JobList.as_view(), name='all'),
    url(r'^(?P<pk>\d+)/', views.JobDetailView.as_view(), name='job_detail'),
    url(r'^delete/(?P<pk>\d+)/', views.DeleteJobView.as_view(), name='job_delete'),
    url(r'^update/(?P<pk>\d+)/', views.UpdateJobView.as_view(), name='job_update'),
    url(r'^add$', views.CreateJobView.as_view(), name='add'),
]
