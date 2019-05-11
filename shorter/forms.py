from django import forms

from .models import Url
from .utils import code_url, current_user


class ShorterForm(forms.ModelForm):
    url = forms.CharField(widget=forms.TextInput(
                          attrs={'placeholder': 'Your URL',
                                 'class': 'form-control', }), label='')

    class Meta:
        model = Url
        fields = ('url', )

    def clean_url(self):
        url = self.cleaned_data['url']

        if 'http' not in url:
            url = 'http://' + url
        if url[-1] != '/':
            url = url + '/'
        return url
