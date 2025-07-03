from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ['name', 'description', 'product', 'due_date']
