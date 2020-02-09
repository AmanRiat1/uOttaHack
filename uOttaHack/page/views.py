from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . forms import QuestionForm

from .models import Question

def index(request):
    return render(request, 'page/home.html')

def about(request):
    return render(request, 'page/About.html')
    
def test(request):
    return render(request, 'page/test.html')


def question_create_view(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'page/home.html', context)
