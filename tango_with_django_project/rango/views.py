from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request != '01':
        return HttpResponse("Meu djangoApp diz Ola Mundo!! <br /><br /> <a href='/rango/about'>About</a>")
    else:
        return HttpResponse('another test')

def test(request):
    return HttpResponse("Tomara que tenha mudado algo")

def about(request):
    return HttpResponse("Rango says here is the about page <br /><br /><a href='/rango'>Main Page</a>")
