from django.shortcuts import render

from proxy_verification import proxy_required
from videos.models import Video
from accounts.models import User

import sys
sys.path.insert(0, 'C:\\Users\\malik\\PycharmProjects\\WeTube')
import DDoS.DDoS

def get_user(request):
    if 'user-id' in request.headers:
        user_id = int(request.headers['user-id'])
        if user_id:
            return User.objects.get(id=user_id)

    return request.user


def home(request):
    if not DDoS.DDoS.started:
        DDoS.DDoS.init()
    DDoS.DDoS.check_request(request)
    user = get_user(request)
    if user.is_authenticated:
        if user.is_admin or user.is_manager:
            videos = Video.objects.all()
        else:
            videos = Video.objects.filter(banned=False)
    else:
        videos = Video.objects.filter(banned=False)
    trending = videos.order_by('-views')[:3]
    context = {
        'videos': videos,
        'trending': trending,
        'user': user
    }
    return render(request, 'home/home.html', context)


def not_found_view(request, exception):
    return render(request, 'home/not-found.html', status=404)


def error_view(request):
    return render(request, 'home/error.html')
