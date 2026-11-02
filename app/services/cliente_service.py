"""
Servicio de Cliente
Lógica de negocio para gestión de clientes
"""

from app.models.cliente import Cliente

class ClienteService:
    """Servicio para operaciones de clientes"""
    
    def __init__(self):
        self.clientes = {}
        self.next_id = 1
    
    def crear_cliente(self, nombre, email, url_sitio=None):
        """Crea un nuevo cliente"""
        
        # Validar datos
        if not nombre or not email:
            return {
                'error': 'Nombre y email son requeridos',
                'success': False
            }
        
        cliente_id = str(self.next_id)
        self.next_id += 1
        
        cliente = Cliente(nombre, email, url_sitio)
        self.clientes[cliente_id] = cliente
        
        return {
            'success': True,
            'cliente_id': cliente_id,
            'cliente': cliente.to_dict()
        }
    
    def obtener_analisis(self, cliente_id):
        """Obtiene historial de análisis de un cliente"""
        if cliente_id not in self.clientes:
            return []
        
        return []
    
    def obtener_resumen(self, cliente_id):
        """Obtiene resumen de un cliente"""
        if cliente_id not in self.clientes:
            return {'error': 'Cliente no encontrado'}
        
        cliente = self.clientes[cliente_id]
        return {
            'cliente': cliente.to_dict(),
            'total_analisis': cliente.analisis_realizados
        }
