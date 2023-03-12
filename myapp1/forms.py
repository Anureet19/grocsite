from django import forms
from .models import OrderItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'client', 'total_items_ordered']
        labels = {
            'total_items_ordered': 'Quantity',
            'client': 'Client Name'
        }
        widgets = {
            'client': forms.RadioSelect()
        }
