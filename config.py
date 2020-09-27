import os

class Config:
    '''
    General Configuration parent class
    '''
    #<<< changed
    SECRET_KEY = 'nkjJndeTU6RESPMBcdSwqZJKnbhCERsweSC'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') #or \
        #'sqlite:///' + db
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Info'
    SENDER_EMAIL = os.environ.get("MAIL")

    #end>>


class ProdConfig(Config):
    '''
    production configuration child class
    Args:
        Config: parent configuration class with general configuration
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    #<<<changed
    DEBUG = True
    #end<<
    
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    #<<<changed
    DEBUG = True
    DEVELOPMENT = True
    #end>>
config_options = {
'development':DevConfig,
'production':ProdConfig
}
