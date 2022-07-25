from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts import views

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.show_account, name='account'),
    path('ticket/', views.send_ticket, name='ticket'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
