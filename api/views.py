import string
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, 'home.html')

def is_match(request):
    try:
        if request.method == 'GET':
            message = request.GET['message']
            pattern = request.GET['pattern']

            def match_check(msg:string, ptn:string):
                if (len(msg)==0 and len(ptn)==0):
                    return True
                if ((len(msg)==0 and len(ptn)>0) or (len(msg)>0 and len(ptn)==0)):
                    return False
                elif (msg[0] == ptn[0] or ptn[0] == '?'):
                    return match_check(msg[1:] ,ptn[1:])
                elif (ptn[0] == '*'):
                    return True
                return False

            body = {
                'is_match' : match_check(message, pattern)
            }

            return HttpResponse(json.dumps(body), status=200)
    
    except:

        body = {
                'is_match' : None
        }
        
        return HttpResponse(json.dumps(body), status=400)

