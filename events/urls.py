from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail/(?P<pk>\d+)', views.detail),
]