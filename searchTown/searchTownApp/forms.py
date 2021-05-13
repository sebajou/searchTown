# from django import forms
from django.contrib.gis import forms
from .models import Town

# from django.contrib.gis.geos import GEOSGeometry

# import re
# from django.contrib.gis.geos import Point
# from django.core.exceptions import ValidationError
# from django.utils.encoding import force_text
# from django.utils.translation import ugettext_lazy as _


# class SimplePointField(forms.Field):
#     default_error_messages = {
#         'invalid': _('Enter latitude,longitude'),
#     }
#     re_point = re.compile(r'^\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*$')
#
#     def prepare_value(self, value):
#         if isinstance(value, Point):
#             return "{},{}".format(*value.coords)
#         return value
#
#     def to_python(self, value):
#         """
#         Validates input. Returns a Point instance or None for empty values.
#         """
#         value = super(SimplePointField, self).to_python(value)
#         if value in self.empty_values:
#             return None
#         try:
#             m = self.re_point.match(force_text(value))
#             if not m:
#                 raise ValueError()
#             value = Point(float(m.group(1)), float(m.group(2)))
#         except (ValueError, TypeError):
#             raise ValidationError(self.error_messages['invalid'],
#                                   code='invalid')
#
#         return value


class TownForm(forms.ModelForm):
    # center = SimplePointField()

    class Meta:
        model = Town
        # fields = "__all__"
        fields = ["codeTown", "nameTown", "surface", "population", "townPostalcode", "codeRegion", "codeDepartement",
                  "centerCoordinateLat", "centerCoordinateLong"]
        widgets = {
            'codeTown': forms.TextInput(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                       'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                       'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'nameTown': forms.TextInput(attrs={'placeholder': 'Un nouveau nom ?', 'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                        'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                        'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'codeRegion': forms.Select(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                        'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                        'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'codeDepartement': forms.Select(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
                                                       'focus:ring-2 focus:ring-green-600 focus:border-transparent '
                                                       'text-gray-400 font-bold py-2 px-4 rounded-full'}),
            'townPostalcode': forms.TextInput(attrs={'class': 'm-2 border border-2 border-green-200 focus:outline-none '
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
                                                            'focus:ring-2 focus:ring-green-600 '
                                                            'focus:border-transparent text-gray-400 font-bold py-2 '
                                                            'px-4 rounded-full'}),
            # 'center': forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}),
        }
