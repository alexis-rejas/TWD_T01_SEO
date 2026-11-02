"""
Modelo de Cliente
Representa los datos de un cliente que usa la app
"""

from datetime import datetime

class Cliente:
    """Modelo de cliente para guardar historiales de análisis"""
    
    def __init__(self, nombre, email, url_sitio=None):
        self.nombre = nombre
        self.email = email
        self.url_sitio = url_sitio
        self.fecha_registro = datetime.now()
        self.analisis_realizados = 0
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'email': self.email,
            'url_sitio': self.url_sitio,
            'fecha_registro': self.fecha_registro.isoformat(),
            'analisis_realizados': self.analisis_realizados
        }
    
    def incrementar_analisis(self):
        """Incrementa el contador de análisis realizados"""
        self.analisis_realizados += 1
