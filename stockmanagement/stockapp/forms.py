from django import forms

from .models import *


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity', 'receive_quantity', 'receive_by', 'received_date',
                  'issue_quantity', 'issue_date', 'issue_by', 'phone_no', 'issue_to', 'bill_no']

    def clean_category(self):

            category = self.cleaned_data.get('category')
            if not category:
                raise forms.ValidationError('This Field is required')
            return category

    def clean_item_name(self):
            item_name = self.cleaned_data.get('item_name')
            if not item_name:
                raise forms.ValidationError('This field is required')
            return item_name

    def clean_quantity(self):
            quantity = self.cleaned_data.get('quantity')
            if not quantity:
                raise forms.ValidationError('This Field is required')
            return quantity

    def clean_receive_quantity(self):

            receive_quantity = self.cleaned_data.get('receive_quantity')
            if not receive_quantity:
                raise forms.ValidationError('This Field s required')

            return receive_quantity

    def clean_receive_by(self):

            receive_by = self.cleaned_data.get('receive_by')
            if not receive_by:
                raise forms.ValidationError('This Field s required')
            return receive_by

    def clean_receive_date(self):

            receive_date = self.cleaned_data.get('receive_date')
            if not receive_date:
                forms.ValidationError('This field is required')

            return receive_date

    def clean_issue_quantity(self):

            issue_quantity = self.cleaned_data.get('receive_date')
            if not issue_quantity:
                forms.ValidationError('This field is required')

            return issue_quantity

    def clean_issue_date(self):

            issue_date = self.cleaned_data.get('issue_date')
            if not issue_date:
                forms.ValidationError('This field is required')

            return issue_date

    def clean_issue_by(self):

            issue_by = self.cleaned_data.get('issue_by')
            if not issue_by:
                forms.ValidationError('This field is required')
            return issue_by

    def clean_phone_no(self):

            phone_no = self.cleaned_data.get('phone_no')
            if not phone_no:
                forms.ValidationError('This field is required')

            return phone_no

    def clean_issue_to(self):

            issue_to = self.cleaned_data.get('issue_to')
            if not issue_to:
                forms.ValidationError('This field is required')

            return issue_to

    def clean_bill_no(self):

            bill_no = self.cleaned_data.get('bill_no')
            if not bill_no:
                forms.ValidationError('This field is required')
            return bill_no


class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'issue_by', 'bill_no']

class StockUpdateForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity', 'receive_quantity', 'receive_by', 'received_date',
                  'issue_quantity', 'issue_date', 'issue_by', 'phone_no', 'issue_to', 'bill_no']

