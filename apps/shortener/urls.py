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
        r'^shorten/$',
        views.form_handler,
        name='form_handler'
    ),

    url(
        r'^(?P<short_url>[\w_\-\d]+)$',
        views.short_url_redir,
        name='short_url_redir'
    ),
]
