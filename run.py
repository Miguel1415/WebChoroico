"""
@file run.py
@description Punto de entrada para ejecución local (Desarrollo).
@author Miguel Olivera Labrin
"""

from app import create_app
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    # Usamos puerto 5001 como estaba en el código original para evitar conflictos
    app.run(port=5001)
