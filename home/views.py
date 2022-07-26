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


def not_found_view(request, exception):
    return render(request, 'home/not-found.html', status=404)


def error_view(request):
    return render(request, 'home/error.html')
