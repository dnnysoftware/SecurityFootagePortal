from itertools import count
from django.shortcuts import render
from baseapp.src.videos import get_videos_formatted


videos = get_videos_formatted()

def home(request):
    return render(request, 'baseapp/home.html', {'videos': videos})

def footage(request, pk):
    video = None
    for i in videos:
        if i.id == int(pk):
            video = i 
    context = {'video': video}
    return render(request, 'baseapp/footage.html', context)
