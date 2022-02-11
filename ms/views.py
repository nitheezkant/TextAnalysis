#This file is made by me

from django.http import HttpResponse
from django.shortcuts import render
def anal(request):
    djt = request.GET.get('text', ' ')
    rp=request.GET.get('rp','off')
    rpp = request.GET.get('rpp', 'off')

    print(djt,"ll")
    punk='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if(rp=='on'):
        anall=""
        for c in djt:
            if c not in punk:
                anall=anall+c
        p={'pur':'remove punctuation!','analll':anall}
        return render(request, 'anal.html',p)
    elif (rpp == 'on'):
        anall = ""
        for c in djt:
            anall=anall+c.capitalize()
        p = {'pur': 'capitalize all the letters!', 'analll': anall}
        return render(request, 'anal.html', p)
    else:
        return HttpResponse('Error')

def index(request):
    return render(request,'index.html')
   
    
