from django import forms
from .models import Order, Product


class OrderForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ['name', 'description', 'product', 'due_date']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'purchase_link', 'is_apple', 'photo']
