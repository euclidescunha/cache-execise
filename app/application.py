import logging
import inject
import mongoengine
from pymongo import MongoClient

from app import settings as common_settings
from app import config
from app.urls import app

logger = logging.getLogger(__name__)


class Config:

    def __init__(self, config_obj):
        self._config_obj = config_obj

    def __get__(self, name):
        return getattr(self._config_obj, name)

    def get(self, name):
        return self.__get__(name)

    def __getitem__(self, name):
        return self.__get__(name)

    def __getattr__(self, name):
        return self.__get__(name)


class Application:
    """"" This singleton class inject configurations """
    def __init__(self, config_obj="ProductionConfig", urls=None, settings=None):
        config_obj = getattr(common_settings, config_obj)
        logger.info("creating new last recent used with config {}".format(config_obj))

        self._config = Config(config_obj())
        self._app = app
        self._db = self.init_database()

        inject.clear_and_configure(self.configure)
        logger.info("LRU loaded")

    def init_database(self) -> MongoClient:
        logger.info("connecting to mongodb {}..".format(self.config['DATABASE_URI']))
        database_alias = "cache_lru_db"
        return mongoengine.connect(host=self.config['DATABASE_URI'], connect=False, alias=database_alias)

    def get_app(self):
        return self._app

    def configure(self, binder):
        binder.bind(config.ApplicationContext, self)

    @property
    def config(self):
        return self._config

    @property
    def db(self) -> MongoClient:
        return self._db

