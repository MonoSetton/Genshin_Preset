from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import PresetForm
from .models import *


def update_art(request, pk):
    PresetFormSet = inlineformset_factory(Preset, Artifact, fields=('set', 'main', 'first', 'second', 'third', 'fourth',
                                                                    'status',), extra=5, can_delete=False, max_num=5)
    preset = Preset.objects.get(id=pk)
    formset = PresetFormSet(instance=preset)
    if request.method == 'POST':
        formset = PresetFormSet(request.POST, instance=preset)
        if formset.is_valid():
            formset.save()
            return redirect('/details/'+pk)

    return render(request, 'presets/update_art.html', {'formset': formset})


def details(request, pk):
    preset = Preset.objects.get(id=pk)
    artifacts = Artifact.objects.filter(preset=preset)
    return render(request, 'presets\details.html', {'artifacts': artifacts, 'preset': preset})


def create_preset(request):
    if request.method == 'POST':
        form = PresetForm(request.POST)
        if form.is_valid():
            preset = form.save(commit=False)
            preset.author = request.user
            form.save()
            return redirect('/')
    else:
        form = PresetForm()
    return render(request, 'presets\create_preset.html', {'form': form})

