import time
from src.main.core.last_recent_used_redis import GeoDistributedLRURedis
from unittest.mock import patch, MagicMock


class TestGeoDistributedLRURedis:
    @patch('src.main.core.models.model.Localization.save')
    def test_set_two_different_items(self, save):
        lru = GeoDistributedLRURedis()
        lru.set_localization("user", 1, 1, {})
        lru.set_localization("user", 1, 2, {})

        lru.get_localization = MagicMock(return_value=[("user", 1, 1, {}), ("user", 1, 2, {})])
        localizations = lru.get_localization()

        assert len(localizations) == 2
        assert localizations == [("user", 1, 1, {}), ("user", 1, 2, {})]

    @patch('src.main.core.models.model.Localization.save')
    def test_set_two_different_items_two_times(self, save):
        lru = GeoDistributedLRURedis()
        lru.set_localization("user", 1, 1, {})
        lru.set_localization("user", 1, 2, {})
        lru.set_localization("user", 1, 1, {})
        lru.set_localization("user", 1, 2, {})

        lru.get_localization = MagicMock(return_value=[("user", 1, 1, {}), ("user", 1, 2, {})])
        localizations = lru.get_localization()

        assert len(localizations) == 2
        assert localizations == [("user", 1, 1, {}), ("user", 1, 2, {})]

    @patch('src.main.core.models.model.Localization.save')
    def test_set_two_equal_items(self, save):
        lru = GeoDistributedLRURedis()
        lru.set_localization("user", 1, 1, {})
        lru.set_localization("user", 1, 1, {})
        lru.get_localization = MagicMock(return_value=[("user", 1, 1, {})])
        localizations = lru.get_localization()

        assert len(localizations) == 1
        assert localizations == [("user", 1, 1, {})]

    @patch('src.main.core.models.model.Localization.save')
    def test_set_two_equal_items_time_expired(self, save):
        lru = GeoDistributedLRURedis()
        lru.set_localization("user", 1, 1, {})
        lru.set_localization("user", 1, 2, {})
        lru.set_localization("user", 1, 1, {})
        time.sleep(6)
        lru.set_localization("user", 1, 1, {})
        lru.get_localization = MagicMock(return_value=[("user", 1, 1, {}), ("user", 1, 2, {}), ("user", 1, 1, {})])
        localizations = lru.get_localization()

        assert len(localizations) == 3
        assert localizations == [("user", 1, 1, {}), ("user", 1, 2, {}), ("user", 1, 1, {})]


