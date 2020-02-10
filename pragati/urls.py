from django.conf.urls import url
from . import views

app_name = 'pragati'

urlpatterns = [
    url(r'^home', views.HomeView.as_view(), name='home'),
    url(r'^list/', views.IdeaListView.as_view(), name='list'),
    url(r'^idea/', views.IdeaCreateView.as_view(), name='idea'),
    url(r'^(?P<pk>\d+)/', views.IdeaDetailView.as_view(), name='detail'),
]
