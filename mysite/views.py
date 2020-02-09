from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .forms import ContactForm
from django.http import HttpResponse

def _form_view(request, template_name='basic.html', form_class=ContactForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print (name)
            html = "<html><body>It is now .</body></html>"
            return HttpResponse(html)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def basic(request):
    return _form_view(request)

