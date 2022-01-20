from django.shortcuts import render
from django.http import HttpResponse, JsonResponse



def home(request):
    return render(request, 'home.html')

def is_match(request):
    if request.method == 'GET':
        message = request.GET['message']
        pattern = request.GET['pattern']

        status = True
        
        response = {
            'is_match' : status
        }

        return JsonResponse(response)

    # return HttpResponse('<h1>You give me something?</h1>')

