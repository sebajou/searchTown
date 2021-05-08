from django import forms
from .models import Town


class TownForm(forms.ModelForm):
    codeTown = forms.CharField(max_length=20)
    nameTown = forms.CharField(max_length=70)
    centerCoordinateLat = forms.IntegerField()
    centerCoordinateLong = forms.IntegerField()
    surface = forms.IntegerField()
    population = forms.IntegerField()
    """townPostalcode = forms.ManyToManyField(CodesPostaux)
    codeRegion = forms.ForeignKey(Region)
    codeDepartement = forms.ForeignKey(Departement)"""
