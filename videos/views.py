from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Video
from .forms import UploadForm


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
    fields = ['title', 'description', 'file']
    # form_class = UploadForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def watch(request, pk):
    video = Video.objects.get(pk=pk)
    video.views += 1
    video.save()
    comments = video.comment_set.all()
    if video:
        context = {
            'video': video,
            'comments': comments
        }
        return render(request, 'videos/watch.html', context=context)
    else:
        return home(request)
