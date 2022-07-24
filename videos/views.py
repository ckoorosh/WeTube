from django.shortcuts import render
from django.views.generic import DetailView, CreateView
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


class UploadView(CreateView):
    model = Video
    success_url = "/"
    template_name = 'videos/upload.html'
    fields = ['file']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WatchView(DetailView):
    template_name = "videos/watch.html"
    model = Video
