from django.conf.urls import include, url
from django.contrib import admin
from . import views as bviews


urlpatterns = [
    # url(r'^worms/(?P<pk>\w+)$', bviews.worm_detail, name='worm_detail'),
    # url(r'^birds/(?P<pk>\w+)$', bviews.bird_detail, name='bird_detail' ),
    # url(r'^clicks/$', bviews.click_list, name='top_click'),
]
