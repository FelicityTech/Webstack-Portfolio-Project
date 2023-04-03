from django.shortcuts import render, redirect
from gTTS.templatetags.gTTS import say
from django.http import HttpResponse, HttpResponseRedirect

from .models import TextAudio
from .forms import TextAudioForm

# Create your views here.

def home(request):
    return render(request, 'audioapp/index.html')

def audio_create(request):
    if request.method == 'POST':
        text_form = TextAudioForm(request.POST)
        if text_form.is_valid():
            lang = request.POST.get('lang')
            text = request.POST.get('text')
            audio_obj = say(language = lang, text = text)
            text_form.save()
            text_form = TextAudioForm()
            context = {'audio_obj':audio_obj,
            'text_form':text_form,
            }
            return render(request, 'audioapp/audio_details.html',context)
        else:
            return redirect('audioapp:audio-create')
    context = {}
    contex['text_form'] = TextAudioForm()
    return render(request, 'audioapp/audio_create.html', context)

def audio_details(request):
    text_audio = TextAudio.objects.all()
    context = {}
    contex['text_audio'] = TextAudio.objects.all()
    return render(request, 'audioapp/audio_details.html', context)

def audio_delete(request, id):
    text_audio = TextAudio.objects.filter(id=id).delete()
    #text_audio = TextAudio.objects.get(id=id)
    #text_audio.delete()
    return HttpResponseRedirect(reverse('audioapp:audio-details'))
