from rest_framework import serializers
from .models import CodesPostaux, Region, Departement, Town


class CodesPostauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodesPostaux
        fields = ('codePostal')
        read_only_fields = ['codePostal']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('codeRegion', 'nameRegion')
        read_only_fields = ['codeRegion', 'nameRegion']


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ('codeDepartement', 'nameDepartement')
        read_only_fields = ['codeDepartement', 'nameDepartement']


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ('codeTown', 'nameTown', 'centerCoordinateLat', 'centerCoordinateLong', 'surface', 'population')
        read_only_fields = ['codeTown', 'nameTown', 'centerCoordinateLat', 'centerCoordinateLong', 'surface',
                            'population']
