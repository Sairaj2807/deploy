from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_message, name='schedule'),
    path('success/', views.success, name='success'),
    path('status/', views.message_status, name='status'),
]
