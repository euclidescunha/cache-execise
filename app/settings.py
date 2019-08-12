import os


class Config:
    DEBUG = False
    TESTING = False

    COOKIE_SECRET = os.environ.get("COOKIE_SECRET", 'COOKIE_SECRET')
    SECRET_KEY = os.getenv('SECRET_KEY')

    DATABASE_URI = None

    MAXCONNECTIONS = os.getenv('MAXCONNECTIONS', 100)
    MAXUSAGE = os.getenv('MAXUSAGE', 300)

    def __init__(self):
        pass


class ProductionConfig(Config):

    def __init__(self):
        super(ProductionConfig, self).__init__()


class StagingConfig(Config):

    def __init__(self):
        super(StagingConfig, self).__init__()


class DevelopmentConfig(Config):
    DEBUG = True

    def __init__(self):
        super(DevelopmentConfig, self).__init__()


class TestingConfig(Config):
    TESTING = True

    def __init__(self):
        super(TestingConfig, self).__init__()

