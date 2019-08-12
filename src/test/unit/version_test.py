from src.main.core.version import comparing_versions


def test_version_one_equals_version_two():
    assert comparing_versions("1.5", "1.5") == 'Version 1.5 is equals 1.5'
    assert comparing_versions("1.5.3", "1.5.3") == 'Version 1.5.3 is equals 1.5.3'


def test_version_one_bigger_version_two():
    assert comparing_versions("1.6", "1.5") == 'Version 1.6 is bigger than 1.5'
    assert comparing_versions("1.6.3", "1.6") == 'Version 1.6.3 is bigger than 1.6'


def test_version_one_lower_version_two():
    assert comparing_versions("1.5", "1.6") == 'Version 1.5 is smaller than 1.6'
    assert comparing_versions("1.5", "1.5.3") == 'Version 1.5 is smaller than 1.5.3'

