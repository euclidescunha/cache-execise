import os


class Config:
    DEBUG = False
    TESTING = False

    COOKIE_SECRET = os.environ.get("COOKIE_SECRET", 'COOKIE_SECRET')
    SECRET_KEY = os.getenv('SECRET_KEY')

    DATABASE_URI = None
    REDIS_URI = None

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
        self.REDIS_URI = os.environ.get(
            "REDIS_URI",
            'redis://{0}:{1}/{2}'.format(
                self.REDIS_HOST,
                self.REDIS_PORT,
                self.REDIS_DATABASE,
            )
        )


class ProductionConfig(Config):
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', 27017)
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'cache_lru')

    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)
    REDIS_DATABASE = os.getenv('REDIS_DATABASE', 0)

    def __init__(self):
        super(ProductionConfig, self).__init__()


class StagingConfig(Config):
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', 27017)
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'cache_lru')

    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)
    REDIS_DATABASE = os.getenv('REDIS_DATABASE', 0)

    def __init__(self):
        super(StagingConfig, self).__init__()


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', 27017)
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'cache_lru')

    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)
    REDIS_DATABASE = os.getenv('REDIS_DATABASE', 0)

    def __init__(self):
        super(DevelopmentConfig, self).__init__()


class TestingConfig(Config):
    TESTING = True
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', 27017)
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'cache_lru')

    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)
    REDIS_DATABASE = os.getenv('REDIS_DATABASE', 0)

    def __init__(self):
        super(TestingConfig, self).__init__()

