"""
Configuración de la aplicación
"""

import os

class Config:
    """Configuración base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-secret-123'
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    DEVELOPMENT = True

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    DEVELOPMENT = False

class TestingConfig(Config):
    """Configuración para testing"""
    TESTING = True
    DEBUG = True

# Seleccionar configuración según entorno
env = os.environ.get('FLASK_ENV', 'development')
if env == 'production':
    Config = ProductionConfig
elif env == 'testing':
    Config = TestingConfig
else:
    Config = DevelopmentConfig
