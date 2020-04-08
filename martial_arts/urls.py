from django.urls import path
from . import views

urlpatterns = [
    path('', views.location_list, name='location_list'),
    path('classes/', views.class_schedule_list, name='class_schedule_list'),
    path('location/<int:pk>', views.location_detail, name='location_detail'),
    path('classes/<int:pk>', views.class_schedule_detail, name='class_schedule_detail'),
]