from django import forms
from .models import Town


class TownForm(forms.ModelForm):
    class Meta:
        model = Town
        fields = "__all__"
