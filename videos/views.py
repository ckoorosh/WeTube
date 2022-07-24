from django.shortcuts import render
from django.views.generic import DetailView
from .models import Video


def home(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'videos/home.html', context)


def login(request):
    return render(request, 'videos/login.html')


def signup(request):
    return render(request, 'videos/signup.html')


def upload(request):
    if request.user.is_authenticated:
        print('YES')
        return render(request, 'videos/upload.html')
    else:
        return render(request, 'videos/login.html')


def watch(request):
    if request.method == "POST":
        query = request.POST.get('id', None)
        if query:
            results = VidStream.objects.filter(title__contains=query)
            return render(request, 'stream/search.html', {'videos': results})

    return render(request, 'videos/home.html')


class WatchView(DetailView):
    template_name = "videos/watch.html"
    model = Video
