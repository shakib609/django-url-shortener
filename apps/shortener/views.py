from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .forms import ShortURLForm
from .models import ShortURL
from .tools import shorten_url
from .serializers import ShortURLSerializer


def homepage(request):
    domain = request.get_host()
    form = ShortURLForm()
    return render(
        request, 'shortener/homepage.html',
        {'form': form, 'domain': domain})


@api_view(['POST'])
def create_short_url(request):
    url = request.data.get('url')
    short_url = shorten_url(get_next_id())
    data = {'url': url, 'short_url': short_url}
    serializer = ShortURLSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def short_url_redir(request, short_url):
    short_urls = ShortURL.objects.filter(short_url=short_url)
    if short_urls:
        url = short_urls[0].url
        return redirect(url)
    else:
        messages.error(request, 'Sorry! The short url doesn\'t exist.')
        return redirect(reverse('shortener:homepage'))


def get_next_id():
    i = ShortURL.objects.last()
    if i is None:
        i = 1
    else:
        i = i.id + 1
    return i
