#!/usr/bin/env python
"""
Script para ejecutar la aplicación
Punto de entrada principal
"""

from app import create_app
from flask import send_file
import os

app_instance = create_app()

# Servir sitemap.xml desde la raíz
@app_instance.route('/sitemap.xml')
def serve_sitemap():
    return send_file(os.path.join(os.path.dirname(__file__), 'sitemap.xml'), mimetype='application/xml')

# Servir robots.txt desde la raíz
@app_instance.route('/robots.txt')
def serve_robots():
    return send_file(os.path.join(os.path.dirname(__file__), 'robots.txt'), mimetype='text/plain')

if __name__ == '__main__':
    print(f"🚀 Iniciando aplicación...")
    print("📚 Abre tu navegador y ve a: http://localhost:8000")
    print("⏹️  Presiona Ctrl+C para detener")
    
    app_instance.run(debug=True, host='0.0.0.0', port=8000)
