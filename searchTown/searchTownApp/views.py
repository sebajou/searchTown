from django.shortcuts import render, redirect, get_object_or_404
from .models import Town, CodesPostaux
from .forms import TownForm
from django.views.generic import ListView, DetailView
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


def edit(request, pk, template_name='searchTownApp/edit.html'):
    """Allow editing of a Town detail. """
    if request.method == 'POST':
        town = Town.objects.get(pk=pk)
        form = TownForm(request.POST, instance=town)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = TownForm()
    return render(request, template_name, {'form': form})


def show(request, pk):
    """Page to display detail about a Town"""
    town = Town.objects.get(pk=pk)
    townPostalcode = town.townPostalcode.all()
    return render(request, "searchTownApp/town_detail.html", {'town': town, 'townPostalcode': townPostalcode})


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
    search_fields = ['nameTown', 'townPostalcode__codePostal']
    filter_backends = (filters.SearchFilter,)
    queryset = Town.objects.all()
    serializer_class = TownSerializer


def search_around_point(request):
    """Allow search around a Town functionality. """
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        dist = request.POST.get('dist')
        pnt = Point(float(lat), float(lon))
        result_around_point = Town.objects.filter(center__distance_lte=(pnt, D(km=dist)))
        return render(request, 'searchTownApp/town_results_around.html', {'result_around_point': result_around_point})
