from src.main.core.x_axis import is_overlaped


def test_is_overlaped():
    assert is_overlaped((1, 5), (4, 8)) is True
    assert is_overlaped((1, 5), (4, 5)) is True


def test_is_not_overlaped():
    assert is_overlaped((1, 5), (6, 8)) is False
    assert is_overlaped((1, 5), (58, 60)) is False
