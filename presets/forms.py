from django.forms import ModelForm
from .models import Preset


class PresetForm(ModelForm):
    class Meta:
        model = Preset
        fields = ['name', 'character', 'weapon']


class PresetUpdateForm(ModelForm):
    class Meta:
        model = Preset
        fields = ['name', 'weapon']
