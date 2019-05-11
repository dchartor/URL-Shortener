from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User

from .utils import code_url
from .validators import validate_url

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=100, validators=[validate_url])
    shortened_url = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if Url.objects.filter(url=self.url, user=self.user).count() == 0:
            self.shortened_url = code_url()
        super(Url, self).save(*args, **kwargs)

    def get_short_url(self):
        url_path = reverse('scode', kwargs={'shortcode': self.shortened_url})
        return 'http://127.0.0.1:8000' + url_path
