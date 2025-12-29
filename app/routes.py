"""
@file app/routes.py
@description Definición de las rutas principales del sitio web.
@author Miguel Olivera Labrin
"""

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    """
    Ruta principal (Home).
    Renderiza la plantilla index.html.
    """
    # TSK-001: Implementación inicial
    return render_template('index.html')

@main.route('/about-us')
def about_us():
    """
    Ruta 'Quiénes Somos'.
    Renderiza la plantilla about_us.html con el contenido correspondiente.
    """
    # TSK-001: Refactorización a Application Factory
    return render_template('about_us.html', section="Quiénes Somos", icon="fa-users")

@main.route('/news')
def news():
    """
    Ruta de 'Noticias'.
    Reutiliza about_us.html como plantilla genérica por ahora.
    """
    # TSK-001: Estandarización a Inglés
    return render_template('about_us.html', section="Noticias", icon="fa-newspaper")

@main.route('/gallery')
def gallery():
    """
    Ruta de 'Galería'.
    Reutiliza about_us.html como plantilla genérica por ahora.
    """
    # TSK-001: Estandarización a Inglés
    return render_template('about_us.html', section="Galería", icon="fa-images")
