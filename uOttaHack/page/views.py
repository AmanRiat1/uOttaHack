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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/test.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})