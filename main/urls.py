from django.urls import path
from main import views

urlpatterns = [
    path("", views.wetherapp, name='home'),
]
