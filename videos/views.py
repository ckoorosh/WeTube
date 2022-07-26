from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from .models import Video, Comment
from .forms import UploadForm


class UploadView(CreateView):
    model = Video
    success_url = "/"
    template_name = 'videos/upload.html'
    fields = ['title', 'description', 'file']

    # form_class = UploadForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def search(request):
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = Video.objects.filter(title__contains=query)
            return render(request, 'videos/search.html', {'videos': results, 'query': query})

    return render(request, 'videos/home.html')


@login_required(redirect_field_name='login')
def send_comment(request, pk):
    if request.method == "POST":
        query = request.POST.get('comment', None)
        if query:
            video = Video.objects.get(pk=pk)
            comment = Comment(body=query, user=request.user, video=video)
            comment.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required(redirect_field_name='login')
def like(request, pk):
    video = Video.objects.get(pk=pk)
    if video:
        user = request.user
        if video.likes.filter(pk=user.pk).exists():
            video.likes.remove(user)
            video.likes_count -= 1
        else:
            if video.dislikes.filter(pk=user.pk).exists():
                video.dislikes.remove(user)
                video.dislikes_count -= 1
            video.likes.add(user)
            video.likes_count += 1
        video.save()
        user.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required(redirect_field_name='login')
def dislike(request, pk):
    video = Video.objects.get(pk=pk)
    if video:
        user = request.user
        if video.dislikes.filter(pk=user.pk).exists():
            video.dislikes.remove(user)
            video.dislikes_count -= 1
        else:
            if video.likes.filter(pk=user.pk).exists():
                video.likes.remove(user)
                video.likes_count -= 1
            video.dislikes.add(user)
            video.dislikes_count += 1
        video.save()
        user.save()

    return redirect(request.META['HTTP_REFERER'])


def add_tag(request, pk):
    if request.user.is_admin:
        video = Video.objects.get(pk=pk)
        if video:
            pass

    return redirect(request.META['HTTP_REFERER'])


def ban(request, pk):
    if request.user.is_admin:
        video = Video.objects.get(pk=pk)
        if video:
            pass

    return redirect(request.META['HTTP_REFERER'])


def watch(request, pk):
    video = Video.objects.get(pk=pk)
    if video:
        video.views += 1
        video.save()
        comments = video.comment_set.all()
        context = {
            'video': video,
            'comments': comments
        }
        return render(request, 'videos/watch.html', context=context)
    else:
        return redirect('home')
