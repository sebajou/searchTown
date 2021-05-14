from django.shortcuts import render, redirect
from .models import Town, Center
from .forms import TownForm
from django.views.generic import ListView
from rest_framework import generics, filters
from .serializers import TownSerializer
import requests
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from searchTown.settings import ALLOWED_HOSTS, DEBUG


class IndexView(ListView):
    """Welcome page"""
    model = Town
    context_object_name = 'town_list'
    template_name = 'searchTownApp/index.html'

    def get_queryset(self):
        town_list = Town.objects.all()
        return town_list


def create(request, template_name='searchTownApp/create.html'):
    """Allow Town creation. """
    if request.method == 'POST':
        # a_town = Town.objects.get(pk=pk)
        form = TownForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print("errors : {}".format(form.errors))
    else:
        form = TownForm()
    return render(request, template_name, {'form': form})


def read(request, pk):
    """Page to display detail about a Town"""
    town = Town.objects.get(pk=pk)
    return render(request, "searchTownApp/town_detail.html", {'town': town})


def update(request, pk, template_name='searchTownApp/edit.html'):
    """Allow editing of a Town detail. """
    town = Town.objects.get(pk=pk)
    if request.method == 'POST':
        form = TownForm(request.POST, instance=town)
        if form.is_valid():
            form.save()
        else:
            print("errors : {}".format(form.errors))
    else:
        form = TownForm()
    return render(request, template_name, {'form': form, 'town': town})


def delete(request, pk, template_name='searchTownApp/confirm_delete.html'):
    """Delete a Town from the database. """
    town = Town.objects.get(pk=pk)
    if request.method == 'POST':
        town.delete()
        return redirect('index')
    return render(request, template_name, {'object': town})


def search_from_endpoint(request):
    """Request to DRF endpoint for search a Town with name or postal code. """
    if request.method == 'POST':
        search_posted = request.POST.get('search_from_endpoint')
        if DEBUG:
            url = 'http://127.0.0.1:8000/town_search/%3Fsearch=?search=' + search_posted
        else:
            url = 'http://134.209.82.129/town_search/%3Fsearch=?search=' + search_posted
        print(url)
        r = requests.get(url)
        search_result = r.json()

        return render(request, 'searchTownApp/town_results_list.html', {'search_result': search_result})


class TownsAPIView(generics.ListCreateAPIView):
    """View of DRF endpoint for search a Town with name or postal code. """
    search_fields = ['nameTown', 'townPostalcode']
    filter_backends = (filters.SearchFilter,)
    queryset = Town.objects.all()
    serializer_class = TownSerializer


def search_around_point(request):
    """Allow search around a Town functionality. """
    if request.method == 'POST':
        # Latitude, longitude of point around where we look for other town
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        pnt = Point(float(lon), float(lat))
        # Distance around the point where look town around
        dist = request.POST.get('dist')
        # Calculate with django.contrib.gis for town around in Center table
        result_around_point_center = Center.objects.filter(center__distance_lte=(pnt, D(km=dist)))
        # Collect codeTown in list from Center table, then filter on Town table with this list
        pk_around = []
        for i in result_around_point_center:
            pk_around.append(i.codeTownCenter.codeTown)
        result_around_point = Town.objects.filter(pk__in=pk_around)

        return render(request, 'searchTownApp/town_results_around.html', {'result_around_point': result_around_point})
