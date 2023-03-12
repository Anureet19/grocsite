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

class InterestForm(forms.Form):
    CHOICES = ((1, 'Yes'), (0, 'No'))
    interested = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    quantity = forms.IntegerField(min_value=1, initial=1)
    comments = forms.CharField(widget=forms.Textarea, label='Additional Comments', required=False)
