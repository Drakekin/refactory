from improved import taxman


def test_basic():
    assert taxman(25000) == 2500


def test_notax():
    assert taxman(10000) == 0


def test_higher():
    assert taxman(75000) == 17500


def test_higher_partial_personal_allowance():
    assert taxman(112500) == 33750


def test_higher_no_personal_allowance():
    assert taxman(130000) == 42000


def test_additional():
    assert taxman(165000) == 56750

