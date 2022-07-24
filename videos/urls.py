from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import UploadView

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('search', views.search, name='search'),
    path('upload', UploadView.as_view(), name='upload'),
    path('comment/<int:pk>/', views.send_comment, name='comment'),
    path('watch/<int:pk>/', views.watch, name='watch')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
