from django.urls import path
from . import views

urlpatterns = [
    path('', views.location_list, name='location_list'),
    path('classes/', views.class_schedule_list, name='class_schedule_list'),
]