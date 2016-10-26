from django.db import models


class ShortURL(models.Model):
    url = models.URLField(default=None)
    short_url = models.CharField(max_length=128, default=None, unique=True)

    def __str__(self):
        return self.url
