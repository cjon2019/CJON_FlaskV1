import os

class Development(object):
    '''
    Development Environment config
    '''
    DEBUG = True
    TESTING = True
    JWT_SECRET_KEY =os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Production(object):
    '''
    Production Environment Config
    '''

    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

app_config = {
    'development': Development,
    'production': Production,
}