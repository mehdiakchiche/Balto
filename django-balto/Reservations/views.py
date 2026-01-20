from django.shortcuts import render
from .models import Reservation

# Création des vues pour mon site web

def accueil(request):
    return render(request, 'Reservations/accueil.html')

def reserver(request):
    if request.method == 'POST':
        Reservation.objects.create(
            nom=request.POST['nom'],
            email=request.POST['email'],
            date=request.POST['date'],
            nombre_personnes=request.POST['nombre_personnes']
        )
    return render(request, 'Reservations/reservation.html')
