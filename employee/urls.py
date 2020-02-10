from django.conf.urls import url
from . import views
#from django.conf import settings
#from django.conf.urls.static import static

app_name='employee'

urlpatterns = [
    url(r'^profile', views.ProfileView.as_view(), name='profile'),
    #url(r'^profileview', views.ProfileDetailView.as_view(), name='profileview_url'),

]


#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

