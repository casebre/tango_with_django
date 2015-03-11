from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'I am a bold font from the context'}
    return render(request, 'rango/index.html', context_dict)

def test(request):
    return HttpResponse("Tomara que tenha mudado algo")

def about(request):
    #return HttpResponse("Rango says here is the about page <br /><br /><a href='/rango'>Main Page</a>")
    qq_merda = {'home': '/rango/'}
    return render(request, 'rango/about.html', qq_merda)
