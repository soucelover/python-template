import pytest

from python_template.example import fibonacci


@pytest.mark.parametrize(
    ("index", "value"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55),
        (20, 6765),
    ],
)
def test_fibonacci(index: int, value: int) -> None:
    assert fibonacci(index) == value
