from django.urls import path

from .views import *
from . import views

app_name = 'locdata'

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('', views.index, name='index'),
    path('<int:locdata_id>', views.detail, name='detail'),
    path('about/', AboutPageView.as_view(), name='about'),
]
