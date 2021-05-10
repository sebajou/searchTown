from django import forms
from .models import Town


class TownForm(forms.ModelForm):
    class Meta:
        model = Town
        # fields = "__all__"
        fields = ["codeTown", "nameTown", "surface", "population", "townPostalcode", "codeRegion", "codeDepartement",
                  "centerCoordinateLat", "centerCoordinateLong"]
