from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
