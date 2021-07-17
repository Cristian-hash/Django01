"""listaContactos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio.views import myHomeView
from inicio.views import anotherView
from personas.views import personaTestView


#tarea
from inicio.views import anotherViewThree
from inicio.views import anotherViewFour
from inicio.views import anotherViewTwo
from personas.views import personaTestView,personaCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myHomeView, name="home"),
    path('another/', anotherView,name="otro"),
    path('persona/', personaTestView, name="otro"),
    path('agregar/',personaCreateView, name="createPersona"),
    

    
    #nuevas  Vistas creadas BASADAS EN FUNCIONES
    path('anotherTwo/',anotherViewTwo),
    path('anotherThree/',anotherViewThree),
    path('anotherFour/',anotherViewFour),
##WARNING GIT
##VISTAS EN CLASES

]
