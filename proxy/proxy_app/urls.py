from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/admin-login/', views.admin_signin, name='admin-login'),
    path('accounts/admin-signup/', views.admin_signup, name='admin-signup'),
    path('accounts/logout/', views.logout_user),
    re_path(r'^accounts/', views.proxy_view),
    re_path(r'^videos/', views.proxy_view),
    re_path(r'^static/', views.proxy_view),
    re_path(r'^media/', views.proxy_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)