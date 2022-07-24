from django.urls import path
from . import views
from . views import WatchView

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('upload', views.upload, name='upload'),
    path('watch/<int:pk>/', WatchView.as_view(), name='watch')
]
