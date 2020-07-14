class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY="sdfs8f7sd96"

    DB_NAME = 'production-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'

    UPLOADS = '/home/oem/PycharmProjects/Flask_app'

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass  

class DevelopmentConfig(Config):

    DEBUG = True


    DB_NAME = 'development-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'


    UPLOADS = "/home/oem/PycharmProjects/Flask_app/app/static/img/uploads"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    DEBUG = True


    DB_NAME = 'testing-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'

    UPLOADS = '/home/oem/PycharmProjects/Flask_app'


    SESSION_COOKIE_SECURE = False







