from django.shortcuts import render, redirect, get_object_or_404
from .models import Town, CodesPostaux
from .forms import TownForm
from django.views.generic import ListView, DetailView
from rest_framework import generics, filters
from .serializers import TownSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class IndexView(ListView):
    model = Town
    context_object_name = 'town_list'
    template_name = 'searchTownApp/index.html'

    def get_queryset(self):
        town_list = Town.objects.all()
        return town_list


class TownDetailView(DetailView):
    model = Town
    template_name = 'searchTownApp/town_detail.html'

"""
def create(request, template_name='searchTownApp/create.html'):
    if request.method == 'POST':
        form = TownForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # return redirect('searchTownApp/town_detail.html')
            except:
                pass
        else:
            form = TownForm()
    return render(request, template_name, {'form': form})"""


def show(request, pk):
    town = Town.objects.get(pk=pk)
    # codePostal = CodesPostaux.objects.get(town=town.codeTown)

    return render(request, "searchTownApp/town_detail.html", {'town': town})


def edit(request, pk, template_name='searchTownApp/edit.html'):
    town = Town.objects.get(pk=pk)
    form = TownForm(request.POST, instance=town)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='searchTownApp/confirm_delete.html'):
    town = Town.objects.get(pk=pk)
    if request.method == 'POST':
        town.delete()
        return redirect('index')
    return render(request, template_name, {'object': town})


class TownsAPIView(generics.ListCreateAPIView):
    search_fields = ['nameTown', 'townPostalcode__codePostal']
    filter_backends = (filters.SearchFilter,)
    queryset = Town.objects.all()
    serializer_class = TownSerializer

# class TownsAPIView(APIView):
#     search_fields = ['nameTown', 'townPostalcode__codePostal']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = TownSerializer
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'town_results_list.html'
#
#     def get(self, request):
#         queryset = Town.objects.all()
#         return Response({'town_results_list': queryset})
