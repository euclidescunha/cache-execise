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
        self.DATABASE_URI = os.environ.get(
            "DATABASE_URI",
            'mongodb://{0}:{1}/{2}'.format(
                self.DATABASE_HOST,
                self.DATABASE_PORT,
                self.DATABASE_NAME,
            )
        )


class ProductionConfig(Config):
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', 27017)
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'cache_lru')

    def __init__(self):
        super(ProductionConfig, self).__init__()


class StagingConfig(Config):
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', 27017)
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'cache_lru')

    def __init__(self):
        super(StagingConfig, self).__init__()


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', 27017)
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'cache_lru')

    def __init__(self):
        super(DevelopmentConfig, self).__init__()


class TestingConfig(Config):
    TESTING = True
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', 27017)
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'cache_lru')

    def __init__(self):
        super(TestingConfig, self).__init__()

