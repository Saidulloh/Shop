from django import forms
from .models import *

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        