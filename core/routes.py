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
    Muestra una galería fotográfica institucional con diseño profesional y lightbox.
    """
    # TSK-007: Datos de ejemplo para la galería
    gallery_items = [
        {
            'id': 1,
            'title': 'Frontis Escuela Aurora',
            'category': 'Infraestructura',
            'image': 'https://images.unsplash.com/photo-1577412647305-991150c7d163?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'description': 'Nuestra hermosa fachada renovada para el año escolar.'
        },
        {
            'id': 2,
            'title': 'Taller de Arte y Cultura',
            'category': 'Actividades',
            'image': 'https://images.unsplash.com/photo-1513364776144-60967b0f800f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'description': 'Estudiantes expresando su creatividad en el taller vespertino.'
        },
        {
            'id': 3,
            'title': 'Laboratorio de Ciencias',
            'category': 'Académico',
            'image': 'https://images.unsplash.com/photo-1576086213369-97a306d36557?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'description': 'Experimentos y aprendizaje práctico en nuestro laboratorio.'
        },
        {
            'id': 4,
            'title': 'Final de Campeonato de Fútbol',
            'category': 'Deportes',
            'image': 'https://images.unsplash.com/photo-1526232761682-d26e03ac148e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'description': 'El equipo de la escuela celebrando su victoria regional.'
        },
        {
            'id': 5,
            'title': 'Biblioteca Escolar',
            'category': 'Infraestructura',
            'image': 'https://images.unsplash.com/photo-1521587760476-6c12a4b040da?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'description': 'Un espacio tranquilo dedicado al estudio y la lectura.'
        },
        {
            'id': 6,
            'title': 'Acto de Fiestas Patrias',
            'category': 'Tradiciones',
            'image': 'https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'description': 'Celebrando nuestras raíces con bailes típicos chilenos.'
        }
    ]
    return render_template('gallery.html', section="Galería", icon="fa-images", photos=gallery_items)
