from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def is_match(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse('<h1>You give me something?</h1>')

