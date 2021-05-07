import pytest
import json
from schema import Schema, And
from searchTown.searchTownApp import scriptRequestGouvApiGeo as script
import ast


class TestsPopDBFromJsonWithCategories:

    def setup_method(self):

        self.schema = Schema([
            {'nom': And(str),
             'code': And(str),
             'codeRegion': And(str),
             'region': And(dict)}])

    @pytest.mark.api_request
    def test_json_departement_region_data_from_api(self):
        schema_json_departement_region = self.schema
        json_to_test = script.json_departement_region_data_from_api("84")
        for dict_to_test in json_to_test:
            assert schema_json_departement_region.is_valid(dict_to_test)


