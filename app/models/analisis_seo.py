"""
Modelo de Análisis SEO
Representa un análisis de SEO realizado
"""

from datetime import datetime

class AnalisisSEO:
    """Modelo para guardar resultados de análisis SEO"""
    
    def __init__(self, titulo, descripcion, palabras_clave, contenido_length, 
                 mobile_friendly, https, fast_load):
        self.titulo = titulo
        self.descripcion = descripcion
        self.palabras_clave = palabras_clave
        self.contenido_length = contenido_length
        self.mobile_friendly = mobile_friendly
        self.https = https
        self.fast_load = fast_load
        self.fecha_analisis = datetime.now()
        self.score = self.calcular_score()
    
    def calcular_score(self):
        """Calcula el score SEO basado en los parámetros"""
        score = 0
        
        # Validar título (0-15 puntos)
        if 30 <= len(self.titulo) <= 60:
            score += 15
        elif len(self.titulo) > 0:
            score += 8
        
        # Validar descripción (0-15 puntos)
        if 120 <= len(self.descripcion) <= 160:
            score += 15
        elif len(self.descripcion) > 0:
            score += 8
        
        # Palabras clave (0-10 puntos)
        if len(self.palabras_clave.split(',')) >= 3:
            score += 10
        elif len(self.palabras_clave) > 0:
            score += 5
        
        # Contenido (0-20 puntos)
        score += 20 if self.contenido_length == 'yes' else 0
        
        # Mobile friendly (0-15 puntos)
        score += 15 if self.mobile_friendly else 0
        
        # HTTPS (0-15 puntos)
        score += 15 if self.https else 0
        
        # Velocidad (0-10 puntos)
        score += 10 if self.fast_load else 0
        
        return min(score, 100)
    
    def obtener_label_score(self):
        """Retorna el label según el score"""
        if self.score >= 70:
            return 'Excelente'
        elif self.score >= 40:
            return 'Necesita mejoras'
        else:
            return 'Muy deficiente'
    
    def to_dict(self):
        return {
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'palabras_clave': self.palabras_clave,
            'score': self.score,
            'label': self.obtener_label_score(),
            'fecha_analisis': self.fecha_analisis.isoformat(),
            'mobile_friendly': self.mobile_friendly,
            'https': self.https,
            'fast_load': self.fast_load
        }
