"""
Aplicación Principal - Optimización SEO de Páginas Web
Inicializador de la aplicación Flask
"""

import os
from flask import Flask
from app.config import Config
from app.routes import seo_routes, cliente_routes

def create_app():
    """Factory para crear la instancia de Flask"""
    # Obtener la ruta del directorio app
    app_dir = os.path.dirname(os.path.abspath(__file__))
    
    app = Flask(__name__, 
                template_folder=os.path.join(app_dir, 'templates'),
                static_folder=os.path.join(app_dir, 'static'),
                static_url_path='/static')
    
    # Cargar configuración
    app.config.from_object(Config)
    
    # Registrar blueprints
    app.register_blueprint(seo_routes.bp)
    app.register_blueprint(cliente_routes.bp)
    
    # Manejo de errores
    @app.errorhandler(404)
    def page_not_found(e):
        return {'error': 'Página no encontrada'}, 404
    
    @app.errorhandler(500)
    def internal_error(e):
        return {'error': 'Error interno del servidor'}, 500
    
    return app
