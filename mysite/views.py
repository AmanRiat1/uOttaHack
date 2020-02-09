import sys
sys.path.append('../')
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .forms import ContactForm
from django.http import HttpResponse
from mysite.model.main import  Main

def _form_view(request, template_name='basic.html', form_class=ContactForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():

            gender = form.cleaned_data['gender_choice']
            if gender == "M":
                gender = 0
            else:
                gender = 1
            age = int(form.cleaned_data['age'])
            family_size = int(form.cleaned_data['family_size'])
            mother_education = int(form.cleaned_data['mother_education'])
            father_education = int(form.cleaned_data['father_education'])
            travel_time_to_school = int(form.cleaned_data['travel_time_to_school'])
            study_time = int(form.cleaned_data['study_time'])
            failures = int(form.cleaned_data['failures'])
            family_support = int(form.cleaned_data['family_support'])
            internet = int(form.cleaned_data['internet'])
            relationship = int(form.cleaned_data['relationship'])
            family_relationship_quality = int(form.cleaned_data['family_relationship_quality'])
            time_after_school = int(form.cleaned_data['time_after_school'])
            going_out = int(form.cleaned_data['going_out'])
            health = int(form.cleaned_data['health'])
            pstatus = int(form.cleaned_data['pstatus'])
            absences = int(form.cleaned_data['absences'])


            model = Main()
            score = model.predict([gender,age,family_size,pstatus,mother_education,father_education,travel_time_to_school,
                                   study_time,failures,family_support,internet,relationship,family_relationship_quality,
                                   time_after_school,going_out,health,absences])
            html = f"<html><body>Your risk of alcohol addiction is {score} .</body></html>"
            return HttpResponse(html)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def basic(request):
    return _form_view(request)

