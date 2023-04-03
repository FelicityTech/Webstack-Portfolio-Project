from django.urls import path
from .import views

app_name = 'audioapp'

urlpatterns = [
    path("", views.index, name = 'home'),
    path('audio-create', views.audio_create, name = 'audio-create'),
    path('audio-details', views.audio_details, name ='audio-details'),
    path('audio-delete/<int:id>', views.audio_delete, name ='audio-delete'),
]