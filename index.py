from app import create_app
from config import ProductionConfig

# Vercel busca una variable llamada 'app' por defecto
app = create_app(ProductionConfig)
