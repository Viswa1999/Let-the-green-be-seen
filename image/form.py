from django import forms
#from django.forms import fields # in-built django forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta: 
        model = Image
        fields=("caption","image")