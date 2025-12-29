"""
@file passenger_wsgi.py
@description Punto de entrada WSGI para cPanel/Phusion Passenger.
@author Miguel Olivera Labrin
"""

import os
import sys

# Agregar el directorio actual al path para que Python encuentre el paquete 'app'
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from config import ProductionConfig

# 'application' es el nombre standard que busca Passenger/cPanel
application = create_app(ProductionConfig)
