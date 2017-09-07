from django.conf.urls import url

from .views import (
    FeiraCreateAPIView,
    FeiraDetailAPIView,
    FeiraDeleteAPIView,
    FeiraListAPIView,
    FeiraUpdateAPIView,
)

urlpatterns = [
    url(r'^$', FeiraListAPIView.as_view(), name='list'),
    url(r'^create/$', FeiraCreateAPIView.as_view(), name='create'),
    url(r'^(?P<id>[\w-]+)/$', FeiraDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>[\w-]+)/edit/$', FeiraUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<id>[\w-]+)/delete/$', FeiraDeleteAPIView.as_view(), name='delete'),
]
