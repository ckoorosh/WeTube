from django.shortcuts import render

from proxy_verification import proxy_required
from videos.models import Video


def home(request):
    if request.user.is_authenticated:
        if request.user.is_admin or request.user.is_manager:
            videos = Video.objects.all()
        else:
            videos = Video.objects.filter(banned=False)
    else:
        videos = Video.objects.filter(banned=False)
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
