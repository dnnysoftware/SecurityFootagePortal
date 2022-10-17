from django.shortcuts import render
from baseapp.src.videos import get_videos_formatted



videos = get_videos_formatted()

def home(request):
    return render(request, 'baseapp/home.html', {'videos': videos})

def footage(request, pk):
    video = None
    for i in videos:
        if i['id'] == int(pk):
            video = i
            if find_if_next(int(pk)+1):
                video['next'] = "../{}".format(int(pk)+1)
            else:
                video['next'] =  "../{}".format(int(pk))
            if int(pk) == 0:
                video['prev'] = "../{}".format(int(pk))
            else:
                video['prev'] =  "../{}".format(int(pk)-1)
    context = {'video': video}
    return render(request, 'baseapp/footage.html', context)

def find_if_next(next):
    for i in videos:
        if i['id'] == int(next):
            return True
    return False

def find_footage(request):
    date_vids = []
    if request.method == 'POST':
        for i in videos:
            if i['date'].strip() == request.POST['date'].strip():
                date_vids.append(i)
    return render(request, 'baseapp/home.html', {'videos': date_vids})



def delete_footage(request, pk):
    print()
