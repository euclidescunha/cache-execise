from src.main.core.x_axis import is_overlaped


class TestIsOverlap:
    def test_is_overlaped(self):
        assert is_overlaped((1, 5), (4, 8)) is True
        assert is_overlaped((1, 5), (4, 5)) is True

    def test_is_not_overlaped(self):
        assert is_overlaped((1, 5), (6, 8)) is False
        assert is_overlaped((1, 5), (58, 60)) is False
