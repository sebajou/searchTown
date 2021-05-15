import pytest
from searchTownApp.models import Town
import fill_db_from_api as fill_bd
from searchTownApp import scriptRequestGouvApiGeo as script


class TestsFillDB:

    @pytest.mark.api_request
    @pytest.mark.transactional_db
    @pytest.mark.django_db(transaction=True)
    def tests_fill_db(self):
        # Verify that database is populate with the dictionary from json file.
        fill_bd()
        # Populate the database with dictionary from json
        instance_pop_bd = script.PopDBFromJson()
        instance_pop_bd.populate_all_db()
        # Stoke data from model in dictionary
        data_from_model = Town.objects.values()
        # Loop to assert that data from dictionary_from_json are stock in the database
        for product_from_model in data_from_model:
            assert str(product_from_model["nameTown"])
            assert float(product_from_model["surface"])