import os

class Config:
    # General Configurations
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    
    # Database Configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///licenses.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # License Management Settings
    LICENSE_VALIDATION_URL = os.environ.get('LICENSE_VALIDATION_URL') or 'https://your-license-validation-url.com'
    LICENSE_EXPIRY_DAYS = 30  # Number of days until a license expires

    # Security Settings
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or 'your_salt_here'
    
    # Logging Configuration
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL') or 'INFO'

# You can create different configurations for different environments
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
