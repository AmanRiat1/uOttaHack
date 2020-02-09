from django.shortcuts import render
from .forms import NameForm
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'page/home.html')

def about(request):
    return render(request, 'page/About.html')
    
def test(request):
    return render(request, 'page/test.html')

def name(request):
    return render(request, 'page/name.html')

def get_name(request):

    form = NameForm()
    return render(request, 'name.html', {'form': form})
