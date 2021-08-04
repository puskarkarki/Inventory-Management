from django.contrib import admin

# Register your models here.
from .forms import *



class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity', 'issue_by', 'phone_no', 'bill_no']
    form = StockCreateForm
    list_filter = ['category', 'item_name', 'issue_by']
    search_fields = ['category', 'item_name', 'issue_by', 'bill_no']


admin.site.register(Stock, StockCreateAdmin)
