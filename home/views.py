from django.db.models import Max
from django.shortcuts import render

from videos.models import Video


def home(request):
    videos = Video.objects.all()
    trending = videos.order_by('-views')[:3]
    context = {
        'videos': videos,
        'trending': trending,
    }
    return render(request, 'home/home.html', context)
