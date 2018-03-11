from django.conf.urls import url, include
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    url(r'^addlisting/$', views.addlisting, name='addlisting'),
    url(r'^mylisting/', views.ListingByUser.as_view(), name='ListingByUser')
]