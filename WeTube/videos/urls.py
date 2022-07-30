from django.urls import path
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from . import views
from .views import UploadView

urlpatterns = [
    path('search/', views.search, name='search'),
    path('upload/', login_required(UploadView.as_view()), name='upload'),
    path('comment/<int:pk>/', views.send_comment, name='comment'),
    path('like/<int:pk>/', views.like, name='like'),
    path('dislike/<int:pk>/', views.dislike, name='dislike'),
    path('tag/<int:pk>/<str:tag>/', views.add_tag, name='tag'),
    path('ban/<int:pk>/', views.ban, name='ban'),
    path('watch/<int:pk>/', views.watch, name='watch')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
