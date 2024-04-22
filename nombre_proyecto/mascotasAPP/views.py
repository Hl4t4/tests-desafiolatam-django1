from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def schnauzer(request):
    return HttpResponse(
    """
    <h1>Mi mascota favorita</h1>
    <p>Esta es mi mascota favorita</p>
    <img src="https://www.publicdomainpictures.net/pictures/40000/velka/dog-schnauzer-portrait.jpg" alt="Schnauzer">
    """)