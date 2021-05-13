from rest_framework import serializers
from .models import Region, Departement, Town, Center


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
        fields = ('codeTown', 'nameTown', 'centerCoordinateLat', 'centerCoordinateLong', 'surface', 'population',
                  'codeRegion', 'codeDepartement', 'townPostalcode')
        read_only_fields = ['codeTown', 'nameTown', 'centerCoordinateLat', 'centerCoordinateLong', 'surface',
                            'population', 'codeRegion', 'codeDepartement', 'townPostalcode']


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ('codeTownCenter', 'center')
        read_only_fields = ['codeTownCenter', 'center']
