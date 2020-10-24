from django import forms
from django.forms import ImageField

from webapp.models import Photo, Favorite


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'label']


class FavoriteAddForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ['id']
