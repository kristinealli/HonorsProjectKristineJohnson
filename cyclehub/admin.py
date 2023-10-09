from django.contrib import admin
from .models import scUser, Item, Trade
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'itemowner', 'photo', 'active', 'available', 'loan_terms', 'created', 'updated',)
admin.site.register(Item, ItemAdmin)

class scUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'profile_photo', 'community', 'phone',)
admin.site.register(scUser, scUserAdmin)

class TradeAdmin(admin.ModelAdmin):
    list_display = ('item', 'borrower', 'borrow_date', 'returned')
admin.site.register(Trade, TradeAdmin)



