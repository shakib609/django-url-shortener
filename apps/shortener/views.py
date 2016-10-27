from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST


from .forms import ShortURLForm
from .models import ShortURL


def homepage(request):
    form = ShortURLForm()
    return render(request, 'shortener/homepage.html', {'form': form})


@require_POST
def form_handler(request):
    form = ShortURLForm(request.POST)
    if form.is_valid():
        url = form.cleaned_data['url']
        short_url = form.cleaned_data['short_url']
        if short_url:
            urls = ShortURL.objects.filter(short_url=short_url)
            if len(urls) > 0:
                messages.error(
                    request,
                    'The short_url exists! Try something else.')
                return redirect(reverse('shortener:homepage'))
        s_url = ShortURL.objects.create(url=url, short_url=short_url)
        messages.success(request, 'URL Shortened successfully!')
        return redirect(reverse('shortener:homepage'))


def short_url_redir(request, short_url):
    short_urls = ShortURL.objects.filter(short_url=short_url)
    if short_urls:
        url = short_urls[0].url
        return redirect(url)
    else:
        messages.error(request, 'Sorry! The short url doesn\'t exist.')
        return redirect(reverse('shortener:homepage'))
