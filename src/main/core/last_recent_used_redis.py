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
        items = json.loads(Localization().get().to_json())

        if number_items and len(items) > number_items:
            return items[-number_items:]

        return items

