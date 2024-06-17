from django.shortcuts import render, HttpResponse

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
