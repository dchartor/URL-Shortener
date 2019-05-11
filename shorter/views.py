from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Url
from .utils import code_url, current_user
from .forms import ShorterForm


class ShortenerView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(Url, shortened_url=shortcode)
        obj.count += 1
        obj.save()
        return HttpResponseRedirect(obj.url)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        get_form = ShorterForm()
        return render(request, 'shorter/home.html', {'form': get_form})

    def post(self, request, *args, **kwargs):
        form = ShorterForm(request.POST)
        user = current_user(request)
        template = 'shorter/home.html'
        context = {
            'form': form,
        }
        if form.is_valid():

            new_url = form.cleaned_data['url']
            obj, created = Url.objects.get_or_create(url=new_url, user=current_user(request))

            if created is False:
                Url.objects.filter(url=new_url, user=user).update(shortened_url=code_url())
                obj = Url.objects.get_or_create(url=new_url, user=user)[0]

            template = 'shorter/list.html'
            context = {
                'obj': obj,
            }

        return render(request, template, context)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UrlListView(ListView):
    model = Url
    context_object_name = 'urls'
    template_name = 'shorter/urls_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = get_list_or_404(Url, user=current_user(self.request))
        return queryset
