from django.shortcuts import render
from django.http import HttpResponse
from django.utils.lorem_ipsum import paragraph

# Create your views here.

def home(request):
    text = paragraph()
    return HttpResponse(
    f"""
    <h1>Pagina de inicio</h1>
    <p>{text}</p>
    """)

def about(request):
    text = paragraph()
    return HttpResponse(
    f"""
    <h1>Acerca de nosotros</h1>
    <p>{text}</p>
    """)

def contact(request):
    text = paragraph()
    return HttpResponse(
    f"""
    <h1>Contacto</h1>
    <form>
        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre"><br>
        <label for="apellido">Apellido:</label><br>
        <input type="text" id="apellido" name="apellido"><br>
        <label for="texto">Texto:</label><br>
        <textarea id="texto" name="texto"></textarea>
    </form> 
    """)