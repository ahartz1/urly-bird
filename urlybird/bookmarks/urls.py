from django.conf.urls import url
from . import views as bviews


urlpatterns = [
    url(r'^worms/(?P<pk>\d+)$',
        bviews.ClickListView.as_view(), name='click_list'),

    url(r'^worms/add$', bviews.add_worm, name='add_worm'),

    url(r'^birds/(?P<pk>\d+)$',
        bviews.BirdListView.as_view(), name='bird_list'),

    url(r'^birds/pop/(?P<pk>\d+)$',
        bviews.BirdPopListView.as_view(), name='bird_pop_list'),

    url(r'^delete/(?P<worm_id>\d+)', bviews.delete_worm, name='delete_worm'),

    url(r'^edit/(?P<worm_id>\d+)', bviews.edit_worm, name='edit_worm'),

    url(r'^popall$', bviews.PopAllListView.as_view(), name='popall_worms'),

    url(r'^pop30$', bviews.Pop30ListView.as_view(), name='pop30_worms'),

    url(r'^popbirds$', bviews.TopBirdsListView.as_view(), name='top_birds'),

    url(r'^$', bviews.WormListView.as_view(), name='recent_worms'),

    url(r'^(?P<slink>[A-Za-z0-9]{7})$',
        bviews.redirect_slink, name='redirect_slink'),

    url(r'^worms/(?P<pk>\d+)/graph$',
        bviews.LineChartJSONView.as_view(), name='line_chart_json'),
]
