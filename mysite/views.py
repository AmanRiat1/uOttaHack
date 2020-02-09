from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .forms import ContactForm
from django.http import HttpResponse

def _form_view(request, template_name='basic.html', form_class=ContactForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender_choice']
            age = form.cleaned_data['age']
            family_size = form.cleaned_data['family_size']
            mother_education = form.cleaned_data['mother_education']
            father_education = form.cleaned_data['father_education']
            travel_time_to_school = form.cleaned_data['travel_time_to_school']
            study_time = form.cleaned_data['study_time']
            failures = form.cleaned_data['failures']
            family_support = form.cleaned_data['family_support']
            internet = form.cleaned_data['internet']
            relationship = form.cleaned_data['relationship']
            family_relationship_quality = form.cleaned_data['family_relationship_quality']
            time_after_school = form.cleaned_data['time_after_school']
            going_out = form.cleaned_data['going_out']
            health = form.cleaned_data['health']

            html = "<html><body>It is now .</body></html>"
            return HttpResponse(html)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def basic(request):
    return _form_view(request)

