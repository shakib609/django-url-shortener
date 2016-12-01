from django.conf.urls import url
from . import views

app_name = 'shortener'
urlpatterns = [
    url(
        r'^$',
        views.homepage,
        name='homepage'
    ),

    url(
        r'^api/$',
        views.create_short_url,
        name='create_short_url_api'
    ),

    url(
        r'^(?P<short_url>[\w_\-\d]+)$',
        views.short_url_redir,
        name='short_url_redir'
    ),
]
