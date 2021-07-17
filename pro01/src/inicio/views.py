from django.shortcuts import render
from django.http import HttpResponse

# from django.http import anotherView
# Create your views here.

#
def myHomeView(request,*args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse('<h1>Hola mundo desde Django</h1>')
#    return render(request,"home.html",{})
def anotherView(request):
    return HttpResponse('<h1>Solo otra pagina</h1>')
#nuevas vistas
def anotherViewTwo(request):
    return HttpResponse('<h1>NUEVA VISTA 2</h1>')

def anotherViewThree(request,*args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"base.html",{})

def anotherViewFour(request,*args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"base2.html",{})
#


#clase 09-06

#def myHomeViewHoy(request,*args,*kwargs):
    
