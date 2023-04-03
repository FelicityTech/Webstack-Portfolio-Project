from django import forms
from django.forms import ModelForm
from .models import TextAudio

class TextAudioForm(ModelForm):
    class Meta:
        model = TextAudio
        exclude =['date_created']

        widgets = {
            'language' : forms.Select()
        }