from django.urls import path
from . import views


app_name = 'exchemuapp'


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    ]