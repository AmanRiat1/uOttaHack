from django.shortcuts import render
from .forms import NameForm
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

<<<<<<< HEAD

def question_create_view(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'page/home.html', context)
=======
def name(request):
    return render(request, 'page/name.html')

def get_name(request):

    form = NameForm()
    return render(request, 'name.html', {'form': form})
>>>>>>> 4751f810dcbaea1ab594834a78889f0f251ab8bd
