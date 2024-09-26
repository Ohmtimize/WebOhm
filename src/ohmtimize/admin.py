from django.contrib import admin

from .models import Installation, Client, Billing, SolarPanel, Device, Consumption, GridExchange, Production
admin.site.register(Installation)
admin.site.register(Client)
admin.site.register(Billing)
admin.site.register(SolarPanel)
admin.site.register(Device)
#admin.site.register(Consumption)
#admin.site.register(GridExchange)
#admin.site.register(Production)


@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ('consumption', 'dateTime', 'user')
    list_filter = ('user',)

@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ('production', 'dateTime', 'user')
    list_filter = ('user',)

@admin.register(GridExchange)
class GridExchangeAdmin(admin.ModelAdmin):
    list_display = ('gridExchange', 'dateTime', 'user')
    list_filter = ('user',) 