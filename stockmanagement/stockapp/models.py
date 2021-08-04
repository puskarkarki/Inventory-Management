from django.db import models
from django.utils import timezone


# Create your models here.

class Stock(models.Model):
    category = models.CharField('Category', max_length=50, blank=True, null=True)
    item_name = models.CharField('Item name', max_length=50, blank=True, null=True)
    quantity = models.DecimalField('Quantity', max_digits=5, decimal_places=2, blank=True, null=True)
    receive_quantity = models.DecimalField('Receive quantity', max_digits=5, decimal_places=2, blank=True, null=True)
    receive_by = models.CharField('Receive by', max_length=51, blank=True, null=True)
    received_date = models.DateTimeField('Received date', default=timezone.now(), blank=True, null=True)
    issue_quantity = models.DecimalField('Issue quantity', max_digits=5, decimal_places=2, blank=True, null=True)
    issue_date = models.DateTimeField('Issue date', default=timezone.now(), blank=True, null=True)
    issue_by = models.CharField('Issue by', max_length=51, blank=True, null=True)
    phone_no = models.CharField('Phone no', max_length=17, blank=True, null=True)
    issue_to = models.CharField('Issue to', max_length=51, blank=True, null=True)
    bill_no = models.CharField('Bill no', max_length=51, blank=True, null=True)
    export_to_csv = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
