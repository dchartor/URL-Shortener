import random
from string import ascii_letters, digits
from django.conf import settings
from django.contrib.auth.models import User

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)


def code_url(size=SHORTCODE_MIN, chars=ascii_letters + digits):
    return ''.join(random.choice(chars) for _ in range(size))


def current_user(request):
    if request.user.is_authenticated:
        return request.user
    else:
        return User.objects.filter(username='guest')[0]
