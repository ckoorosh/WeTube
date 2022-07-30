from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts import views

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('admin-login/', views.admin_signin, name='admin-login'),
    path('signup/', views.signup, name='signup'),
    path('admin-signup/', views.admin_signup, name='admin-signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.show_account, name='account'),
    path('ticket/', views.send_ticket, name='ticket'),
    path('ticket/respond/<int:pk>/', views.respond_ticket, name='respond-ticket'),
    path('ticket/edit/<int:pk>/', views.change_ticket_status, name='change-ticket-status'),
    path('unstrike/<int:pk>/', views.unstrike, name='unstrike'),
    path('verify/<int:pk>/', views.verify, name='verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
