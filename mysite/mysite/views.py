from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request,"Gaurav.html")
    #return HttpResponse("<h1>Hello<h1> <a href=https://data-flair.training/blogs/python-speech-recognition-ai/> DataFlair</a>")
def back(request):
    return HttpResponse('''<a href="/"> You Clicked Back </a>''')
    #return HttpResponse("<h1>About</h1>")
def remove(request):
    return HttpResponse("<h1>You clicked Link</h1>")
def add(request):
    return HttpResponse("<h1>You clicked Action</h1>")
def cut(request):
    return HttpResponse("<h1>You clicked Another Action</h1>")
def submit(request):
    otext=text=request.POST.get("text","default")
    check1=request.POST.get("check1","off")
    check2=request.POST.get("check2","off")
    check3=request.POST.get("check3","off")

    if check1=="on":
        text=text.upper()
        parameter={"task":"Upper","text":text}
    if check2=="on":
        text2=""
        punc='''!@#$%^&*()_+{}:"<>?][;',./='''
        for i in text:
            if not(i in punc):
                text2=text2+i
            text=text2
        parameter={"task":"Removing Special Chacter","text":text}
    if check3=="on":
        text2=""
        number='''1234567890'''
        for i in text:
            if not(i in number):
                text2=text2+i
        text=text2
        parameter={"task":"Removing number","text":text}
        
    
    
    return render(request,"Analyse.html",parameter)
