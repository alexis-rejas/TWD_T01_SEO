"""
Rutas de SEO
Endpoints para análisis y consultas SEO
"""

from flask import Blueprint, render_template, request, jsonify
from app.services.seo_service import SEOService

bp = Blueprint('seo', __name__)
seo_service = SEOService()

@bp.route('/', methods=['GET'])
def index():
    """Página principal de SEO"""
    return render_template('base.html')

@bp.route('/seo/analizar', methods=['POST'])
def analizar_seo():
    """Endpoint para analizar SEO de una página"""
    datos = request.get_json()
    
    resultado = seo_service.analizar(
        titulo=datos.get('titulo', ''),
        descripcion=datos.get('descripcion', ''),
        palabras_clave=datos.get('palabras_clave', ''),
        contenido_length=datos.get('contenido_length', ''),
        mobile_friendly=datos.get('mobile_friendly', False),
        https=datos.get('https', False),
        fast_load=datos.get('fast_load', False)
    )
    
    return jsonify(resultado)

@bp.route('/seo/consejos', methods=['GET'])
def obtener_consejos():
    """Obtiene consejos de SEO según categoría"""
    categoria = request.args.get('categoria', 'general')
    consejos = seo_service.obtener_consejos(categoria)
    return jsonify({'consejos': consejos})

@bp.route('/seo/metricas', methods=['GET'])
def obtener_metricas():
    """Obtiene métricas de SEO del caso real"""
    metricas = seo_service.obtener_metricas_caso_real()
    return jsonify(metricas)
