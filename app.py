from core import create_app
from config import ProductionConfig

print("Iniciando aplicación en Vercel...")

# Vercel busca una variable llamada 'app' por defecto
app = create_app(ProductionConfig)

# Test routes to debug 404
@app.route('/')
def v_home():
    return "Home direct from app.py (core package)"

@app.route('/vercel-test')
def vercel_test():
    return "Vercel connects to app.py successfully!"
