from django import forms
from django.forms import ImageField

from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'label', 'author']
