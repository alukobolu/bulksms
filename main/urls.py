from django.urls import path, include
from . import views
app_name = "main_api"

urlpatterns = [
    path('home', views.gethome, name='home'),# get
    path('home/send', views.posthome, name='send'),# post
    path('logout', views.postlogout, name='sendlogout'),# post
]