import pytest
import json
from schema import Schema, And
from searchTownApp.models import Town
from searchTownApp import scriptRequestGouvApiGeo as script
import ast


class TestsPopDBFromJsonWithCategories:

    def setup_method(self):

        self.schema_region_data = Schema(
            {'nom': And(str),
             'code': And(str)})

        self.schema_departement_region = Schema(
            {'nom': And(str),
             'code': And(str),
             'codeRegion': And(str),
             'region': And(dict)})

        self.schema_commune = Schema(And(dict))

        """with open("communes_26.json", "r") as read_file:
            self.json_for_test = json.load(read_file)"""

    @pytest.mark.api_request
    def test_json_region_data_from_api(self):
        schema_region_data = self.schema_region_data
        instance_pop_bd = script.PopDBFromJson()
        json_to_test = instance_pop_bd.json_region_data_from_api("11")
        for dict_to_test in json_to_test:
            assert schema_region_data.is_valid(dict_to_test)

    @pytest.mark.api_request
    def test_json_departement_region_data_from_api(self):
        schema_json_departement_region = self.schema_departement_region
        instance_pop_bd = script.PopDBFromJson()
        json_to_test = instance_pop_bd.json_departement_region_data_from_api("84")
        for dict_to_test in json_to_test:
            assert schema_json_departement_region.is_valid(dict_to_test)

    @pytest.mark.api_request
    def test_json_communes_data_from_api(self):
        schema_json_communes = self.schema_commune
        instance_pop_bd = script.PopDBFromJson()
        json_to_test = instance_pop_bd.json_communes_data_from_api("26")
        print(json_to_test)
        for dict_to_test in json_to_test:
            assert schema_json_communes.is_valid(dict_to_test)

    """
    @pytest.mark.django_db(transaction=True)
    def tests_pop_db(self):
        1Verify that database is populate with the dictionary from json file.
        json_for_test = self.json_for_test
        # Populate the database with dictionary from json
        instance_pop_bd = script.PopDBFromJson()
        instance_pop_bd.pop_communes_db(data_communes_json=json_for_test)
        # Stoke data from model in dictionary
        dictionary_from_model = Town.objects.values()
        # Loop to assert that data from dictionary_from_json are stock in the database
        for product_from_model in dictionary_from_model:
            assert str(product_from_model["name"])
            """


