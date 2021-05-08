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
                                    'centerCoordinateLong': 0, 'surface':0, 'population':2, 'codeRegion':' 77777',
                                    'codeDepartement': '7777'}

    @pytest.mark.django_db
    def tests_IndexView(self):
        response = c.get('/town/')
        assert response.status_code == 200

    def tests_TownDetailView(self):
        pass

    @pytest.mark.django_db
    def tests_show(self):
        response = c.get('/town/26004')
        assert response.status_code == 301

    # @pytest.mark.django_db
    # def tests_create(self):
    #     response = c.get('/town/create/')
    #     assert response.status_code == 301

    # @pytest.mark.django_db
    # def tests_edit(self):
    #     create_request = self.town_create_request
    #     response = c.post('/town/edit/', create_request)
    #     response = c.get('/town/edit/26004/')
    #     assert response.status_code == 301

    def tests_delete(self):
        pass
