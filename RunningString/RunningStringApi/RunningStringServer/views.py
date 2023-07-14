from wsgiref.util import FileWrapper

from MainRunner.Main import run
from RunningStringServer.models import History
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


def index(request):
    records = History.objects.all()
    for history in records:
        print(history.id)
        print(history.s)
    return render(request, 'home_page.html', {'history': records})


def create_request(request):
    if request.method == 'POST':
        history = History()
        history.s = request.POST.get('s')
        history.save()
        run(history.s)
        return HttpResponseRedirect("/")


def download_file(request):
    if request.method == 'GET':
        file = FileWrapper(
            open('C:/Users/deimo/projects/itsolution/RunningString/RunningStringApi/cache/output_video.mp4', 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename= running_string.mp4'
        return response
