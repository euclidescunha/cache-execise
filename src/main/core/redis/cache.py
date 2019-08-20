from redis import StrictRedis


class RedisClient:
    def __init__(self):
        """This could be better config """
        self._redis = StrictRedis("localhost")

    def redis(self):
        return self._redis


