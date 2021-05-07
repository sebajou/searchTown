import requests
import json
from .models import CodesPostaux, Region, Departement, Town
import string
import pickle
import re


class PopDBFromJson:
    """Request https://geo.api.gouv.fr to optain json then populate database. """

    def __init__(self):
        self.list_codes_region = ['1', '2', '3', '4', '6', '11', '24', '27', '28', '32', '44', '52', '53', '75', '76',
                                  '84', '93', '94']

    @staticmethod
    def json_region_data_from_api(code_region):
        """
        Request https://geo.api.gouv.fr/departements?codeRegion=codes_region&fields=nom,code,codeRegion,region
        to obtain from region code list data about region in a json.
        """

        url = 'https://geo.api.gouv.fr/regions?code=' + code_region + '&fields=nom,code'
        req = requests.get(url)
        data_region_json = req.json()

        return data_region_json

    @staticmethod
    def json_departement_region_data_from_api(codes_region):
        """
        Request https://geo.api.gouv.fr/departements?codeRegion=codes_region&fields=nom,code,codeRegion,region
        to obtain from region code list data about region and departement in a json.
        """

        url = "https://geo.api.gouv.fr/departements?codeRegion=" + codes_region + "&fields=nom,code,codeRegion,region"
        req = requests.get(url)
        data_departement_region_json = req.json()

        return data_departement_region_json

    @staticmethod
    def json_communes_data_from_api(codes_departement):
        """
        Request https://geo.api.gouv.fr/departements/26/communes?fields=nom,code,codesPostaux,centre,surface,
        codeDepartement,departement,codeRegion,region&format=json&geometry=centre'
        to obtain from region code list data about region and departement in a json.
        """

        url = "https://geo.api.gouv.fr/departements/" + codes_departement + \
              "/communes?fields=nom,code,codesPostaux,centre,surface,codeDepartement,departement,codeRegion,region," \
              "population&format=json&geometry=centre'"
        req = requests.get(url)
        data_communes_json = req.json()

        return data_communes_json

    @staticmethod
    def pop_region_db(data_region_json):
        """Populate the database table of region with the json_region_data_from_api file."""
        for region_inside_json in data_region_json:
            if Region.objects.filter(codeRegion=region_inside_json["code"]):
                pass
            else:
                region = Region(codeRegion=region_inside_json["code"], nameRegion=region_inside_json["nom"])
                region.save()

    @staticmethod
    def pop_departement_db(data_departement_region_json):
        """Populate the database table of region and departement with the json_departement_region_data_from_api file."""
        for dep_inside_json in data_departement_region_json:
            # Populate departement columns
            if Departement.objects.filter(codeDepartement=dep_inside_json["code"]):
                pass
            else:
                r = Region.objects.get(codeRegion=dep_inside_json["region"]["code"])
                departement = Departement(nameDepartement=dep_inside_json["nom"],
                                          codeDepartement=dep_inside_json["code"],
                                          codeRegion=r)
                departement.save()

    @staticmethod
    def pop_communes_db(data_communes_json):
        """Populate the database table of communes with the data_communes_json file."""
        for communes_inside_json in data_communes_json:
            # Update database if Town already exist
            if Town.objects.filter(codeTown=communes_inside_json["code"]):
                r = Region.objects.get(codeRegion=communes_inside_json["region"]["code"])
                d = Departement.objects.get(codeDepartement=communes_inside_json["departement"]["code"])
                existing_town = Town.objects.get(codeTown=communes_inside_json["code"])
                existing_town.codeTown = communes_inside_json["code"]
                existing_town.nameTown = communes_inside_json["nom"]
                existing_town.centerCoordinateLat = (communes_inside_json["centre"]["coordinates"][0]*10000)
                existing_town.centerCoordinateLong = (communes_inside_json["centre"]["coordinates"][1]*10000)
                existing_town.surface = (communes_inside_json["surface"]*100)
                existing_town.population = communes_inside_json["population"]
                existing_town.codeRegion = r
                existing_town.codeDepartement = d
                existing_town.save()

            else:
                r = Region.objects.get(codeRegion=communes_inside_json["region"]["code"])
                d = Departement.objects.get(codeDepartement=communes_inside_json["departement"]["code"])
                town = Town(codeTown=communes_inside_json["code"],
                             nameTown=communes_inside_json["nom"],
                             centerCoordinateLat=(communes_inside_json["centre"]["coordinates"][0]*10000),
                             centerCoordinateLong=(communes_inside_json["centre"]["coordinates"][1]*10000),
                             surface=(communes_inside_json["surface"]*100),
                             population=communes_inside_json["population"],
                             codeRegion=r,
                             codeDepartement = d)
                town.save()
                if CodesPostaux.objects.filter(codePostal=communes_inside_json["codesPostaux"][0]):
                    pass
                else:
                    town.townPostalcode.create(codePostal=communes_inside_json["codesPostaux"][0])

    def populate_all_db(self):
        region_code_list = self.list_codes_region
        # Populate region data
        for region_code in region_code_list:
            json_region = self.json_region_data_from_api(region_code)
            self.pop_region_db(json_region)
        # Populate departement data
        for region_code in region_code_list:
            json_departement = self.json_departement_region_data_from_api(region_code)
            self.pop_departement_db(json_departement)
        # Create list of departement code
        departement_query = Departement.objects.all().values_list('codeDepartement')
        departement_list = []
        for departement in departement_query:
            departement_list.append(departement[0])
        # Populate commune and postal code data
        for departement in departement_list:
            json_communes = self.json_communes_data_from_api(departement)
            self.pop_communes_db(json_communes)
