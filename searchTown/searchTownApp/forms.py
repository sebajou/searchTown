from django import forms
from .models import Town


class TownForm(forms.ModelForm):
    class Meta:
        model = Town
        # fields = "__all__"
        fields = ["codeTown", "nameTown", "surface", "population", "townPostalcode", "codeRegion", "codeDepartement",
                  "centerCoordinateLat", "centerCoordinateLong"]
        widgets = {
            'codeTown': forms.TextInput(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                       'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                       'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'nameTown': forms.TextInput(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                        'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                        'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'codeRegion': forms.Select(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                        'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                        'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'codeDepartement': forms.Select(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                       'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                       'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'townPostalcode': forms.Select(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                            'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                            'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'surface': forms.NumberInput(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                            'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                            'text-gray-400 font-bold py-2 px-4 rounded-full'}),

            'centerCoordinateLat': forms.NumberInput(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                         'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                         'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'centerCoordinateLong': forms.NumberInput(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                         'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                         'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'population': forms.NumberInput(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                'text-gray-400 font-bold py-2 px-4 rounded-full'}),

        }