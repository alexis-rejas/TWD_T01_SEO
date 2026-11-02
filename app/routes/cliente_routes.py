"""
Rutas de Cliente
Endpoints para gestión de clientes y sus análisis
"""

from flask import Blueprint, request, jsonify, render_template
from app.services.cliente_service import ClienteService

bp = Blueprint('cliente', __name__, url_prefix='/cliente')
cliente_service = ClienteService()

@bp.route('/registrar', methods=['POST'])
def registrar_cliente():
    """Registra un nuevo cliente"""
    datos = request.get_json()
    
    resultado = cliente_service.crear_cliente(
        nombre=datos.get('nombre'),
        email=datos.get('email'),
        url_sitio=datos.get('url_sitio')
    )
    
    return jsonify(resultado), 201

@bp.route('/<cliente_id>/analisis', methods=['GET'])
def obtener_analisis_cliente(cliente_id):
    """Obtiene historial de análisis de un cliente"""
    analisis = cliente_service.obtener_analisis(cliente_id)
    return jsonify({'analisis': analisis})

@bp.route('/<cliente_id>/resumen', methods=['GET'])
def obtener_resumen_cliente(cliente_id):
    """Obtiene resumen de un cliente"""
    resumen = cliente_service.obtener_resumen(cliente_id)
    return jsonify(resumen)
