"""
Servicio de SEO
Lógica de negocio para análisis y operaciones SEO
"""

from app.models.analisis_seo import AnalisisSEO

class SEOService:
    """Servicio para operaciones de SEO"""
    
    def __init__(self):
        self.analisis_historial = []
    
    def analizar(self, titulo, descripcion, palabras_clave, contenido_length, 
                 mobile_friendly, https, fast_load):
        """Realiza un análisis completo de SEO"""
        
        analisis = AnalisisSEO(
            titulo=titulo,
            descripcion=descripcion,
            palabras_clave=palabras_clave,
            contenido_length=contenido_length,
            mobile_friendly=mobile_friendly,
            https=https,
            fast_load=fast_load
        )
        
        self.analisis_historial.append(analisis)
        
        # Generar recomendaciones
        recomendaciones = self._generar_recomendaciones(analisis)
        
        return {
            'score': analisis.score,
            'label': analisis.obtener_label_score(),
            'recomendaciones': recomendaciones,
            'detalles': analisis.to_dict()
        }
    
    def _generar_recomendaciones(self, analisis):
        """Genera recomendaciones basadas en el análisis"""
        recomendaciones = []
        
        if len(analisis.titulo) < 30 or len(analisis.titulo) > 60:
            recomendaciones.append({
                'tipo': 'titulo',
                'mensaje': 'El título debe tener entre 30-60 caracteres',
                'severidad': 'alta'
            })
        
        if len(analisis.descripcion) < 120 or len(analisis.descripcion) > 160:
            recomendaciones.append({
                'tipo': 'descripcion',
                'mensaje': 'La descripción debe tener entre 120-160 caracteres',
                'severidad': 'alta'
            })
        
        if not analisis.mobile_friendly:
            recomendaciones.append({
                'tipo': 'responsive',
                'mensaje': 'Tu sitio debe ser adaptable a dispositivos móviles',
                'severidad': 'crítica'
            })
        
        if not analisis.https:
            recomendaciones.append({
                'tipo': 'seguridad',
                'mensaje': 'Implementa HTTPS para mejorar seguridad y rankings',
                'severidad': 'crítica'
            })
        
        if not analisis.fast_load:
            recomendaciones.append({
                'tipo': 'velocidad',
                'mensaje': 'Optimiza la velocidad de carga de tu sitio',
                'severidad': 'alta'
            })
        
        return recomendaciones
    
    def obtener_consejos(self, categoria):
        """Obtiene consejos SEO por categoría"""
        consejos_db = {
            'on_page': [
                {
                    'titulo': 'Optimizar Títulos',
                    'descripcion': 'El título debe tener entre 30-60 caracteres e incluir la palabra clave principal'
                },
                {
                    'titulo': 'Escribir Meta Descripciones',
                    'descripcion': 'La descripción debe resumir el contenido en 120-160 caracteres'
                },
                {
                    'titulo': 'Usar Headers HTML',
                    'descripcion': 'Estructura el contenido con H1, H2, H3 para mejorar la jerarquía'
                }
            ],
            'tecnico': [
                {
                    'titulo': 'HTTPS Obligatorio',
                    'descripcion': 'Implementa certificado SSL para seguridad'
                },
                {
                    'titulo': 'Sitemap XML',
                    'descripcion': 'Crea un sitemap.xml para que Google indexe mejor'
                },
                {
                    'titulo': 'Robots.txt',
                    'descripcion': 'Configura robots.txt para controlar el rastreo'
                }
            ],
            'contenido': [
                {
                    'titulo': 'Contenido de Calidad',
                    'descripcion': 'Escribe mínimo 300 palabras con valor para el usuario'
                },
                {
                    'titulo': 'Palabras Clave',
                    'descripcion': 'Investiga y usa palabras clave relevantes naturalmente'
                },
                {
                    'titulo': 'Enlaces Internos',
                    'descripcion': 'Enlaza páginas relacionadas para mejorar la navegación'
                }
            ]
        }
        
        return consejos_db.get(categoria, consejos_db['on_page'])
    
    def obtener_metricas_caso_real(self):
        """Obtiene métricas del caso real del restaurante"""
        return {
            'caso': 'Restaurante La Tratoria',
            'metricas': {
                'trafico_organico_antes': 0,
                'trafico_organico_despues': 1200,
                'unidad_trafico': 'visitas/mes',
                'ranking_antes': 'No indexado',
                'ranking_despues': '#3',
                'keyword': 'Restaurante italiano Madrid',
                'reservas_mensuales': 50,
                'rating_google': 4.8,
                'numero_resenas': 42,
                'roi': {
                    'inversion': 1500,
                    'periodo_meses': 6,
                    'clientes_nuevos': 85,
                    'ingresos_generados': 12750
                }
            }
        }
