from redis_cache import RedisCache
from src.main.core.models.model import Localization
from src.main.core.redis.cache import RedisClient
import json


class GeoDistributedLRURedis:
    redis_client = RedisClient()
    cache = RedisCache(redis_client=redis_client.redis())
    ttl = 30
    maxsize = 10

    @staticmethod
    @cache.cache(ttl=ttl, limit=maxsize)
    def set_localization(user, latitude: float, longitude: float, information: dict):
        print("cache")
        localization = Localization()
        localization.user = user
        localization.latitude = latitude
        localization.longitude = longitude
        localization.information = information
        localization.save()

        return json.loads(localization.to_json())

    @staticmethod
    @cache.cache(ttl=ttl, limit=maxsize)
    def get_localization(number_items: int = None):
        localization = Localization.objects().all()

        if number_items and localization.count() > number_items:
            return json.loads(localization.to_json())[-number_items:]
        return json.loads(localization.to_json())

