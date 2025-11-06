from django.contrib import admin
from medico.models import BlackMarketItem, InventoryItem, Consultation, Traitement

# Register your models here.
admin.site.register(Consultation)
admin.site.register(Traitement)
admin.site.register(BlackMarketItem)
admin.site.register(InventoryItem)
