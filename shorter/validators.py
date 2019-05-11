from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(url):
    url_validator = URLValidator()
    reg_value = url
    if 'http' in reg_value:
        new_value = reg_value
    else:
        new_value = 'http://' + url
    try:
        url_validator(new_value)
    except:
        raise ValidationError('Invalid URL')
    return new_value
