from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .forms import ShortURLForm
from .models import ShortURL


def homepage(request):
    form = ShortURLForm()
    return render(request, 'shortener/homepage.html', {'form': form})


def short_url_redir(request, short_url):
    short_urls = ShortURL.objects.filter(short_url=short_url)
    if short_urls:
        url = short_urls[0].url
        return redirect(url)
    else:
        messages.error(request, 'Sorry! The short url doesn\'t exist.')
        return redirect(reverse('shortener:homepage'))
