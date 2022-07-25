from django.shortcuts import render

from videos.models import Video


def home(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'home/home.html', context)
