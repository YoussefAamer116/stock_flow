from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['item', 'quantity_sold']

    def clean_quantity_sold(self):
        quantity_sold = self.cleaned_data.get('quantity_sold')
        if quantity_sold <= 0:
            raise forms.ValidationError('Quantity sold must be positive.')
        return quantity_sold