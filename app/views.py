from django.shortcuts import render

# Create your views here.
def imgroot(request) :
    return render(request, 'app/index.html', {})

def index(request) :
    return render(request, 'app/test.html', {})