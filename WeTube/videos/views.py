from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView

from proxy_verification import proxy_required
from .models import Video, Comment, Tag
from accounts.models import User
from .forms import UploadForm
from django.core.exceptions import ValidationError


def get_user(request):
    if 'user-id' in request.headers:
        user_id = int(request.headers['user-id'])
        if user_id:
            return User.objects.get(id=user_id)

    return request.user

def file_size(value):
    limit = 50 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 50 MiB.')

class UploadView(CreateView):
    model = Video
    success_url = "/"
    template_name = 'videos/upload.html'
    fields = ['title', 'description', 'file']

    # form_class = UploadForm
    #
    # def not_admin(self):
    #     return not self.request.user.is_admin
    #
    # @user_passes_test(not_admin)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(UploadView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        tag = Tag()
        tag.save()
        form.instance.tag = tag
        return super().form_valid(form)


def search(request):
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = Video.objects.filter(title__contains=query)
            return render(request, 'videos/search.html', {'videos': results, 'query': query, 'user': get_user(request)})

    return render(request, 'videos/home.html', context={'user': get_user(request)})


@login_required(redirect_field_name='login')
def send_comment(request, pk):
    user = get_user(request)
    if request.method == "POST":
        query = request.POST.get('comment', None)
        if query:
            video = Video.objects.get(pk=pk)
            comment = Comment(body=query, user=user, video=video)
            comment.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required(redirect_field_name='login')
def like(request, pk):
    video = Video.objects.get(pk=pk)
    if video:
        user = get_user(request)
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
        user = get_user(request)
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


@proxy_required
def add_tag(request, pk, tag):
    user = get_user(request)
    if user.is_admin:
        video = Video.objects.get(pk=pk)
        if video:
            video.tag.set_tag(tag)

    return redirect('watch', pk)


@proxy_required
def ban(request, pk):
    user = get_user(request)
    if user.is_admin:
        video = Video.objects.get(pk=pk)
        if video:
            if video.banned:
                video.un_ban()
            else:
                video.ban()
                user = video.user
                user_videos = user.video_set.all()
                video_index = list(user_videos.values_list('id', flat=True)).index(video.id)
                if video_index > 0:
                    previous_video = user_videos[video_index - 1]
                    if previous_video.banned:
                        user.set_strike(True)
                if video_index < len(user_videos) - 1:
                    next_video = user_videos[video_index + 1]
                    if next_video.banned:
                        user.set_strike(True)

    return redirect('watch', pk)


def watch(request, pk):
    video = Video.objects.get(pk=pk)
    if video:
        video.views += 1
        video.save()
        comments = video.comment_set.all()
        context = {
            'video': video,
            'comments': comments,
            'user': get_user(request)
        }
        return render(request, 'videos/watch.html', context=context)
    else:
        return redirect('home')
