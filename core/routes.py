"""
@file core/routes.py
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
    Muestra un feed de noticias institucionales con diseño profesional.
    """
    # TSK-006: Datos de ejemplo para el feed de noticias
    news_items = [
        {
            'id': 1,
            'title': 'Inauguración del Año Escolar 2025',
            'excerpt': 'Damos la bienvenida a nuestros estudiantes para un nuevo ciclo de aprendizaje y crecimiento integral.',
            'date': '05 Mar 2025',
            'category': 'Evento',
            'image': 'noticia_escuela_1.jpg',
            'icon': 'fa-graduation-cap'
        },
        {
            'id': 2,
            'title': 'Éxito en la Feria Científica Regional',
            'excerpt': 'Nuestros alumnos de 8vo básico obtuvieron el primer lugar con su proyecto de sustentabilidad.',
            'date': '20 Nov 2024',
            'category': 'Académico',
            'image': 'noticia_escuela_2.jpg',
            'icon': 'fa-flask'
        },
        {
            'id': 3,
            'title': 'Nueva Alianza de Deportes Choroico',
            'excerpt': 'Firmamos un convenio para fomentar el deporte y la vida sana entre nuestros jóvenes deportistas.',
            'date': '15 Nov 2024',
            'category': 'Deportes',
            'image': 'noticia_escuela_3.jpg',
            'icon': 'fa-medal'
        },
        {
            'id': 4,
            'title': 'Taller de Robótica y Programación',
            'excerpt': 'Iniciamos nuevos talleres tecnológicos para desarrollar las habilidades del siglo XXI en nuestros estudiantes.',
            'date': '10 Nov 2024',
            'category': 'Tecnología',
            'image': 'noticia_escuela_4.jpg',
            'icon': 'fa-robot'
        }
    ]
    return render_template('news.html', section="Noticias", icon="fa-newspaper", news=news_items)

@main.route('/gallery')
def gallery():
    """
    Ruta de 'Galería'.
    Reutiliza about_us.html como plantilla genérica por ahora.
    """
    # TSK-001: Estandarización a Inglés
    return render_template('about_us.html', section="Galería", icon="fa-images")
