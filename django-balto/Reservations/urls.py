from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil),
    path('reservation/', views.reserver),
]