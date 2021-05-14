import pytest
import json
from schema import Schema, And
from searchTownApp.models import Town
from searchTownApp import scriptRequestGouvApiGeo as script
import ast
from django.test import Client

c = Client()


class TestsPopDBFromJsonWithCategories:

    def setup_method(self):
        self.town_create_request = {'codeTown': '777', 'nameTown': 'Paradis', 'centerCoordinateLat': 0,
                                    'centerCoordinateLong': 0, 'surface': 0, 'population': 2, 'codeRegion': ' 84',
                                    'codeDepartement': '73'}
        self.town_update_request = {'codeTown': '777', 'nameTown': 'Tartare', 'centerCoordinateLat': 0,
                                    'centerCoordinateLong': 0, 'surface': 0, 'population': 2, 'codeRegion': ' 84',
                                    'codeDepartement': '73'}
        self.search_from_endpoint_name = 'Saint-Ismier'
        self.search_from_endpoint_code = '26300'
        self.schema_endpoint = Schema(And(list))
        self.search_around = {'lat': 45.5, 'lon': 5.5, 'dist': 5.0}

    def tests_IndexView(self):
        response = c.get('/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def tests_get_create(self):
        response = c.get('/town/create/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def tests_post_create(self):
        create_request = self.town_create_request
        response = c.post('/town/create/', create_request)
        assert response.status_code == 200

    @pytest.mark.django_db
    def tests_read(self):
        response = c.get('/town/read/26004')
        assert response.status_code == 301

    @pytest.mark.django_db
    def tests_update(self):
        create_request = self.town_create_request
        update_request = self.town_update_request
        response = c.post('/town/create/', create_request)
        response_final = c.post('/town/update/777/', update_request)
        assert response_final.status_code == 200

    @pytest.mark.django_db
    def tests_delete(self):
        create_request = self.town_create_request
        response = c.post('/town/create/', create_request)
        response_final = c.get('/town/delete/777/')
        assert response_final.status_code == 200

    @pytest.mark.django_db
    def tests_search_from_endpoint_town_name(self):
        search = self.search_from_endpoint_name
        schema_endpoint = self.schema_endpoint
        search_on_endpoint = '/town_search/%3Fsearch=?search' + search
        response = c.get(search_on_endpoint)
        assert schema_endpoint.is_valid(response.json())

    @pytest.mark.django_db
    def tests_search_from_endpoint_town_code(self):
        search = self.search_from_endpoint_code
        schema_endpoint = self.schema_endpoint
        search_on_endpoint = '/town_search/%3Fsearch=?search' + search
        response = c.get(search_on_endpoint)
        assert schema_endpoint.is_valid(response.json())

    @pytest.mark.django_db
    def tests_search_around_point(self):
        search_around = self.search_around
        response = c.post('/searchTownApp/town_results_around', search_around)
        assert response.status_code == 200
