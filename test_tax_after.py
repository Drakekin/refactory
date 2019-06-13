from optimised import taxman


def test_basic():
    assert taxman(25000) == 2500


def test_notax():
    assert taxman(10000) == 0


def test_higher():
    assert taxman(75000) == 17500


def test_additional():
    assert taxman(165000) == 54250
