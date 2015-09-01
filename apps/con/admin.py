from django.contrib import admin
from models import Item, Dinar
# Register your models here.

class DinarAdmin(admin.ModelAdmin):
    list_display=["name","inicial","fim"]

class ItemAdmin(admin.ModelAdmin):
    list_display=["name","nombre","price","dinar","isException"]
"""
class PeriodAdmin(admin.ModelAdmin):
    list_display=["inicial","fim","valid_period"]
"""
admin.site.register(Dinar, DinarAdmin)
admin.site.register(Item,ItemAdmin)
#admin.site.register(Period, PeriodAdmin)
