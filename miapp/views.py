from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Evaluación de la Capacidad 3</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>EVALUACIÓN DE LA CAPACIDAD 3 - GRUPO (EL MEJOR)</h1>
                <hr/>
            </div>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <a class="navbar-brand" href="/inicio">Inicio</a>
            </nav>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <a class="navbar-brand" href="/primos">Primos</a>
            </nav>
"""

footer = """
            <hr/>
            <div class="footer">
                <p>&copy; 2024 Grupo (El Mejor)</p>
            </div>
        </div>
    </body>
    </html>
"""

def index(request):
    mensaje = """
        <div>
            <h2 class="text-primary">LENGUAJE DE PROGRAMACIÓN 3</h2>
            <ul class="team-list">
                <li>Dafne Ayelen Huertas Gonzales</li>
                <li>Arian Erick Sevillano Colina</li>
                <li>Diego Jheremy Caballero Villazana</li>
                <li>Andre Rafael Fernandez Huaman</li>
            </ul>
        </div>
    """
    return HttpResponse(layout + mensaje + footer)

def es_primo(num):
    """ Función auxiliar para verificar si un número es primo """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primos(request, a=0, b=100):
    if a>b:
        return redirect('primos',a=b, b=a)
    resultado = f"""
        <h2> Números de [{a},{b}] </h2> 
    """
    
    a = int(a)  # Convertir a y b a enteros, ya que vienen desde request
    b = int(b)
    
    while a <= b:
        if es_primo(a):
            resultado += f"<li> {a} </li>"
        a += 1
    
    resultado += "</ul>"
    return HttpResponse(layout + resultado + footer)

