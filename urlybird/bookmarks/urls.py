from django.conf.urls import include, url
from django.contrib import admin
from . import views as bviews


urlpatterns = [
    # url(r'^worms/(?P<pk>\w+)$', bviews.worm_detail, name='worm_detail'),
    url(r'^birds/(?P<pk>\w+)$', bviews.BirdListView.as_view(), name='bird_detail'),
    url(r'^$', bviews.WormListView.as_view(), name='recent_worms'),
    ]
