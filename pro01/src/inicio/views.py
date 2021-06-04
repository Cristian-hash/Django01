from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(*args,**kwargs):
    #
    return HttpResponse('<h1>Hola mundo desde Django</h1>')
#    return render(request,"home.html",{})
def anotherView(request):
    return HttpResponse('<h1>Solo otra pagina</h1>')
