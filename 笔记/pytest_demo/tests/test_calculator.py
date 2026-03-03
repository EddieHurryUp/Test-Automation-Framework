import pytest


def test_add(calc):
    assert calc.add(1, 2) == 3


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (8, 2, 4),
        (5, 2, 2.5),
        (-9, 3, -3),
    ],
)
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected


def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="b cannot be 1"):
        calc.divide(10, 0)

