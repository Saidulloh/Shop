from django import forms
from django.forms.widgets import TextInput
from .models import *

class SocialSidebarForm(forms.ModelForm):
    class Meta:
        model = SocialSidebar
        fields = '__all__'
        widgets = {
            'background': TextInput(attrs={'type': 'color'}),
        }
