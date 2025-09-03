from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    # begin normal validation -----------------------------------------
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Your Product Name',
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Your Product Description',
        'rows': '3',
        'cols': '50',
    }))
    price = forms.DecimalField(initial=100.89)

    # end normal validation ---------------------------------------------

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    # custom validation rules ---------------------------------
    def clean_name(self):
        name = self.cleaned_data['name']
        if "Orange" in name:
            return name
        else:
            raise forms.ValidationError("Orange should be in name!")

    # end custom validation rule ------------------------------


class RawProductForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder' : 'Your Product Name',
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder' : 'Your Product Description',
        'rows' : '3',
        'cols' : '50',
    }))
    price = forms.DecimalField(initial=100.89)