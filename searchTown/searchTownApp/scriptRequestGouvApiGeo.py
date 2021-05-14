import requests
from .models import Region, Departement, Town, Center
from django.contrib.gis.geos import Point


class PopDBFromJson:
    """Request https://geo.api.gouv.fr to obtain json then populate database. """

    def __init__(self):
        self.list_codes_region = ['1', '2', '3', '4', '6', '11', '24', '27', '28', '32', '44', '52', '53', '75', '76',
                                  '84', '93', '94']
        self.list_codes_departement = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
                                       '14', '15', '16', '17', '18', '19', '2A', '2B', '21', '22', '23', '24', '25',
                                       '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38',
                                       '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51',
                                       '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64',
                                       '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77',
                                       '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
                                       '91', '92', '93', '94', '95', '971', '972', '973', '974']

    @staticmethod
    def json_region_data_from_api(code_region):
        """
        Request https://geo.api.gouv.fr/regions?code=code_region&fields=nom,code
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
        """Populate the database table of region with the data_communes_json file."""
        for regions_inside_json in data_region_json:
            if Region.objects.filter(codeRegion=regions_inside_json["region"]["code"]):
                    pass
            else:
                region = Region(codeRegion=regions_inside_json["region"]["code"],
                                nameRegion=regions_inside_json["region"]["nom"])
                region.save()

    @staticmethod
    def pop_departement_db(data_departement_region_json):
        """Populate the database table of region and departement with the json_departement_region_data_from_api file."""
        for dep_inside_json in data_departement_region_json:
            # Populate departement columns
            if Departement.objects.filter(codeDepartement=dep_inside_json["departement"]["code"]):
                pass
            else:
                r = Region.objects.get(codeRegion=dep_inside_json["region"]["code"])
                departement = Departement(nameDepartement=dep_inside_json["departement"]["nom"],
                                          codeDepartement=dep_inside_json["departement"]["code"],
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
                existing_town.centerCoordinateLat = (communes_inside_json["centre"]["coordinates"][0])
                existing_town.centerCoordinateLong = (communes_inside_json["centre"]["coordinates"][1])
                existing_town.surface = (communes_inside_json["surface"])
                existing_town.population = communes_inside_json["population"]
                existing_town.codeRegion = r
                existing_town.codeDepartement = d
                existing_town.save()

            # Fill Town and Center table
            else:
                r = Region.objects.get(codeRegion=communes_inside_json["region"]["code"])
                d = Departement.objects.get(codeDepartement=communes_inside_json["departement"]["code"])
                town = Town(codeTown=communes_inside_json["code"],
                            nameTown=communes_inside_json["nom"],
                            centerCoordinateLat=(communes_inside_json["centre"]["coordinates"][1]),
                            centerCoordinateLong=(communes_inside_json["centre"]["coordinates"][0]),
                            surface=(communes_inside_json["surface"]),
                            townPostalcode=(communes_inside_json["codesPostaux"][0]),
                            population=communes_inside_json["population"],
                            codeRegion=r,
                            codeDepartement=d)
                town.save()
                # Fill Center table (one to one relastionship with Town table)
                if Center.objects.filter(codeTownCenter=communes_inside_json["code"]):
                    pass
                else:
                    print("before center fill")
                    c = Center(codeTownCenter=town, center=Point(communes_inside_json["centre"]["coordinates"][0],
                                                                      communes_inside_json["centre"]["coordinates"][1]))
                    c.save()
                    print("after center fill")

    def populate_all_db(self):
        """Execute all method of PopDBFromJson class to populate database. """
        region_code_list = self.list_codes_region
        departement_list = self.list_codes_departement

        for departement in departement_list:
            json_departement = self.json_communes_data_from_api(departement)
            # Populate region table
            self.pop_region_db(json_departement)
            # Populate departement table
            self.pop_departement_db(json_departement)
            # Populate Town and Center table
            self.pop_communes_db(json_departement)

