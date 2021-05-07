from django.shortcuts import render, redirect, get_object_or_404
from .models import Town
from .forms import TownForm
from django.views.generic import ListView, DetailView


# Create your views here.

class IndexView(ListView):
    template_name = 'searchTownApp/index.html'
    context_object_name = 'town_list'

    def get_queryset(self):
        return Town.objects.all()


class ContactDetailView(DetailView):
    model = Town
    template_name = 'searchTownApp/town-detail.html'


def create(request):
    if request.method == 'POST':
        form = TownForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TownForm()

    return render(request, 'searchTownApp/create.html', {'form': form})


def edit(request, pk, template_name='searchTownApp/edit.html'):
    town = get_object_or_404(Town, pk=pk)
    form = TownForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='searchTownApp/confirm_delete.html'):
    town = get_object_or_404(Town, pk=pk)
    if request.method == 'POST':
        town.delete()
        return redirect('index')
    return render(request, template_name, {'object': town})

