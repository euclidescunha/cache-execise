from cachetools import cached, TTLCache


class GeoDistributedLRU:
    cache = TTLCache(maxsize=10, ttl=30)

    def __init__(self, max_size=10, ttl=30):
        self.cache.update(maxsize=max_size, ttl=ttl)
        self.coordenades = []

    @cached(cache)
    def set_localization(self, user, latitude: float, longitude: float):
        self.coordenades.append((user, latitude, longitude))

    @cached(cache)
    def get_localization(self, number_items: int = None):
        if number_items and len(self.coordenades) >= number_items:
            return self.coordenades[-number_items:]
        return self.coordenades

