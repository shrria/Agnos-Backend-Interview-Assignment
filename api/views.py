from django.shortcuts import render
from django.http import HttpResponse, JsonResponse



def home(request):
    return render(request, 'home.html')

def is_match(request):
    if request.method == 'GET':
        message = request.GET['message']
        pattern = request.GET['pattern']

        def match_check(msg, ptn):
            if (len(msg)==0 and len(ptn)==0):
                return True
            if ((len(msg)==0 and len(ptn)>0) or (len(msg)>0 and len(ptn)==0)):
                return False
            elif (msg[0] == ptn[0] or ptn[0] == '?'):
                return match_check(msg[1:] ,ptn[1:])
            elif (ptn[0] == '*'):
                return True
            return False

        status = match_check(message, pattern)
        
        response = {
            'is_match' : status
        }

        return JsonResponse(response)

    # return HttpResponse('<h1>You give me something?</h1>')

