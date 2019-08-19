from redis import StrictRedis
from redis_cache import RedisCache
from src.main.core.models.model import Localization
import json

client = StrictRedis(host="0.0.0.0")
cache = RedisCache(redis_client=client)

ttl = 30
maxsize = 10


@cache.cache(ttl=ttl, limit=maxsize)
def set_localization(user, latitude: float, longitude: float):
    print("cache")
    localization = Localization()
    localization.user = user
    localization.latitude = latitude
    localization.longitude = longitude
    localization.save()

    return json.loads(localization.to_json())


@cache.cache(ttl=ttl, limit=maxsize)
def get_localization(number_items: int = None):
    localization = Localization.objects().all()

    if number_items and localization.count() > number_items:
        return json.loads(localization.to_json())[-number_items:]
    return json.loads(localization.to_json())



