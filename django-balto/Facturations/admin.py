from django.contrib import admin
from .models import ClientEntreprise, CarteRFID, Facture, Paiement

admin.site.register(ClientEntreprise)
admin.site.register(CarteRFID)
admin.site.register(Facture)
admin.site.register(Paiement)