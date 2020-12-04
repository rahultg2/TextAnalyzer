# I have created this file - Rahul
from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
#    return HttpResponse("hello")
#     return HttpResponse('''<h1>Rahul</h1> <a
#    href = "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">
#    Django Code With Harry</a>''') #personal navigator

#def about(request):
#    return HttpResponse("About Rahul")

#pipeline
def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed the spaces', 'analyzed_text': analyzed}
        djtext = analyzed


    if charcount == "on":
        analyzed = 0
        for char in djtext:
            if not((char >= '0' and char <= '9') or char == " "):
                analyzed = analyzed + 1
        params = {'purpose': 'Counted characters', 'analyzed_text': analyzed}


    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse("******* No Selection .... Please selectoperations that are provided on the home page *******")
    else:
        return render(request, 'analyze.html', params)
def aboutus(request):
    return render(request, 'about us.html')






