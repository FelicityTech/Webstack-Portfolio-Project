from django.shortcuts import render, redirect
from gTTS.templatetags.gTTS import say
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import TextAudio
from .forms import TextAudioForm

# Create your views here.

def home(request):
    return render(request, 'audioapp/index.html')

def audio_create(request):
    if request.method == 'POST':
        text_form = TextAudioForm(request.POST)
        if text_form.is_valid():
            text_form.save()
            return redirect('audioapp:audio-details')
    else:
        context = {}
        context['text_form'] = TextAudioForm()
    return render(request, 'audioapp/audio_create.html', context)

def audio_details(request):
    text_audio = TextAudio.objects.all()
    context = {}
    context['text_audio'] = TextAudio.objects.all()
    return render(request, 'audioapp/audio_details.html', context)

def audio_modify(request, id):
    text_obj = TextAudio.objects.get(id=id)
    if request.method == 'GET':
        text_form = TextAudioForm(instance=text_obj)
    else:
        text_form = TextAudioForm(request.POST)
        if form.is_valid():
            text_form.save()
            return redirect('audioapp:audio-details')
    return render(request, 'audioapp/audio_modify.html', {'text_form':text_form,})

def audio_delete(request, id):
    text_audio = TextAudio.objects.filter(id=id).delete()
    #text_audio = TextAudio.objects.get(id=id)
    #text_audio.delete()
    return HttpResponseRedirect(reverse('audioapp:audio-details'))
