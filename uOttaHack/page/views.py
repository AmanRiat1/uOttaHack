from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'page/home.html')

def about(request):
    return render(request, 'page/About.html')
    
def test(request):
    return render(request, 'page/test.html')
