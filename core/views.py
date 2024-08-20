from django.shortcuts import render,HttpResponse ##por ahora usamos esto

plantilla="""
<h3>Super Web</h3>
<ul>
    <li> <a href="/">Inicio</a> </li>
    <li> <a href="/gallery/">Galeria</a> </li>
    <li> <a href="/faq/">FAQ</a> </li>
</ul>
"""

# Create your views here.
def home(request):
    return HttpResponse(plantilla+"<p> Hola Mundo </p>")

def gallery(request):
    return HttpResponse(plantilla+"<p> Hola soy la Galeria </p>")

def faq(request):
    return HttpResponse(plantilla+"<p> Hola soy preguntas frecuentes </p>")