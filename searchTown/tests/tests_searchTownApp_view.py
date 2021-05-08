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
        pass

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

    @pytest.mark.django_db
    def tests_create(self):
        response = c.get('/town/create/')
        assert response.status_code == 301

    @pytest.mark.django_db
    def tests_edit(self):
        response = c.get('/town/edit/26004/')
        assert response.status_code == 301

    def tests_delete(self):
        pass
