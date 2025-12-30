from app import create_app
from config import ProductionConfig

print("Iniciando aplicación en Vercel...")

# Vercel busca una variable llamada 'app' por defecto
app = create_app(ProductionConfig)

# Sanity check for Vercel
@app.route('/vercel-test')
def vercel_test():
    return "Vercel connects to index.py successfully!"
