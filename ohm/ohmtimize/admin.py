from django.contrib import admin

from .models import Installation, Client, Billing, SolarPanel, Device, GDPR, Consumption, GridExchange, Production

admin.site.register(Installation)
admin.site.register(Client)
admin.site.register(Billing)
admin.site.register(SolarPanel)
admin.site.register(Device)
admin.site.register(GDPR)
admin.site.register(Consumption)
admin.site.register(GridExchange)
admin.site.register(Production)
