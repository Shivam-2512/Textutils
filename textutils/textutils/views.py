#i have created this file -

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get text
    djtext = request.GET.get('text', 'default')
    #check values form checkbox
    remove_punk = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    if remove_punk == "on":

        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for ch in djtext:
            if ch not in punctuations:
                analyzed += ch
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

        #return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for ch in djtext:
            analyzed += ch.upper()
        params = {'purpose':"Changed to UPPER CASE", 'analyzed_text': analyzed}
        djtext = analyzed

        #return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for ch in djtext:
            if ch != '\n':
                analyzed += ch
        params = {'purpose': "New lines Removed", 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if spaceremover == "on":
        analyzed = ""
        for index, ch in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed += ch
        params = {'purpose': 'Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed

        #return render(request, 'analyze.html', params)

    if charcount == 'on':
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed += 1

        params = {'purpose': "Numbers of characters : ", 'analyzed_text': analyzed}

    if (remove_punk != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcount != 'on'):
        return HttpResponse("Select Karlo kisi ek ko")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def contactdata(request):
    return render(request, 'contactdata.html')