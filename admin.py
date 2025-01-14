from django.contrib import admin
from .models import Stock, Category, History
from .form import StockCreateform
# Register your models here.

class StockCreateAdmin(admin.ModelAdmin):
	list_display = ['category']
	form = StockCreateform
	list_filter = ['category']
	search_fields = ['category']
admin.site.register(Stock, StockCreateAdmin)
#admin.site.register(History)
admin.site.register(History)
admin.site.register(Category)
