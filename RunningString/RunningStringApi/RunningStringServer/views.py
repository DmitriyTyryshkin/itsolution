import os
from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from MainRunner.Main import run
from RunningStringServer.models import History


def index(request):
    records = History.objects.all()
    return render(request, 'home_page.html', {'history': records})

def create_request(request):
    if request.method == 'POST':
        history = History()
        history.s = request.POST.get('s')
        history.save()
        run(history.s)
        FileResponse(open('C:/Users/deimo/projects/itsolution/RunningString/RunningStringApi/cache/output_video.mp4', 'rb'))
        return HttpResponseRedirect("/")

 #render(request, 'home_page.html')  #HttpResponseRedirect("/create")

# тест#255,255,255#0,0,0