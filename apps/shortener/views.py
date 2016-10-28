from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST


from .forms import ShortURLForm
from .models import ShortURL


CHARACTERS = list(
    map(chr, range(97, 123))) + list(
        map(chr, range(65, 91))) + list(map(str, range(0, 10)))


def homepage(request):
    domain = request.get_host()
    form = ShortURLForm()
    return render(
        request, 'shortener/homepage.html',
        {'form': form, 'domain': domain})


@require_POST
def form_handler(request):
    form = ShortURLForm(request.POST)
    if form.is_valid():
        url = form.cleaned_data['url']
        s_url = ShortURL.objects.create(url=url)
        shortened_url = shorten_url(s_url.id)
        s_url.short_url = shortened_url
        s_url.save()
        domain = 'http://' + request.get_host() + '/' + s_url.short_url
        messages.success(request, '''URL Shortened successfully!
        <br/>Share this link: <a href="{0}">{0}</a>'''.format(domain))
        return redirect(reverse('shortener:homepage'))


def short_url_redir(request, short_url):
    short_urls = ShortURL.objects.filter(short_url=short_url)
    if short_urls:
        url = short_urls[0].url
        return redirect(url)
    else:
        messages.error(request, 'Sorry! The short url doesn\'t exist.')
        return redirect(reverse('shortener:homepage'))


def shorten_url(pk):
    pk = int(pk)
    digits = []
    while pk > 0:
        digit = int(pk % 62)
        digits.append(digit)
        pk = int(pk // 62)
    digits.reverse()
    result = ''
    for digit in digits:
        result += CHARACTERS[digit]
    return result
