from django.conf.urls import url
from . import views as bviews


urlpatterns = [
    url(r'^worms/(?P<pk>\w+)$',
        bviews.WormDetailView.as_view(),
        name='worm_detail'),

    url(r'^worms/add$', bviews.add_worm, name='add_worm'),

    url(r'^birds/(?P<pk>\w+)$',
        bviews.BirdListView.as_view(),
        name='bird_detail'),

    url(r'^delete/(?P<worm_id>\d+)', bviews.delete_worm, name='delete_worm'),
    url(r'^edit/(?P<worm_id>\d+)', bviews.edit_worm, name='edit_worm'),
    url(r'^$', bviews.WormListView.as_view(), name='recent_worms'),

]
