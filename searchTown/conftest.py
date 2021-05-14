import pytest
from django.core.management import call_command
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    try:
        with django_db_blocker.unblock():
            call_command('loaddata', 'test_serachTown_v1_db.json', verbosity=1)
        print('conftest for populate test database')
    except:
        print('conftest fail to populate test database')
