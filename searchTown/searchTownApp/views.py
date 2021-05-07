from django.shortcuts import render, redirect, get_object_or_404
from .models import Town, CodesPostaux
from .forms import TownForm
from django.views.generic import ListView, DetailView


# Create your views here.

class IndexView(ListView):
    template_name = 'searchTownApp/index.html'
    context_object_name = 'town_list'

    def get_queryset(self):
        return Town.objects.all()


class TownDetailView(DetailView):
    model = Town
    template_name = 'searchTownApp/town_detail.html'


def show(request, pk):
    town = Town.objects.get(pk=pk)
    # codePostal = CodesPostaux.objects.get(town=town.codeTown)

    return render(request, "searchTownApp/town_detail.html", {'town': town})


def create(request):
    if request.method == 'POST':
        form = TownForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TownForm()

    return render(request, 'searchTownApp/create.html', {'form': form})


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
