from math import isclose

import pytest

from classes.Tests.unit_tests.tasks_from_the_first_module import discriminant, solution


# Тестируем функцию discriminant
@pytest.mark.parametrize("a, b, c, expected", [(1, -3, 2, 1),  # D = (-3)² - 4*1*2 = 1
        (1, -4, 4, 0),  # D = (-4)² - 4*1*4 = 0
        (3, -4, 2, -8),  # D = (-4)² - 4*3*2 = -8
        (1, 0, -4, 16),  # D = 0² - 4*1*(-4) = 16
        (2, 4, 2, 0),  # D = 4² - 4*2*2 = 0
])
def test_discriminant(a, b, c, expected):
    assert discriminant(a, b, c) == expected


# Тестируем функцию solution
@pytest.mark.parametrize("a, b, c, expected", [# Нет корней
        (3, -4, 2, 'корней нет'),

        # Один корень
        (1, -4, 4, 2.0), (4, 4, 1, -0.5), (1, 2, 1, -1.0),

        # Два корня
        (1, -3, 2, (2.0, 1.0)), (1, -5, 6, (3.0, 2.0)), (1, 4, 3, (-1.0, -3.0)), (2, -2, -4, (2.0, -1.0)),

        # Дробные корни
        (1, -1.5, 0.5, (1.0, 0.5)), (2, 0, -1, (0.707, -0.707)), ])
def test_solution(a, b, c, expected):
    result = solution(a, b, c)

    if expected == 'корней нет':
        assert result == expected
    elif isinstance(expected, float):
        assert isclose(result, expected, abs_tol=1e-3)
    else:
        x1, x2 = result
        exp1, exp2 = expected
        assert isclose(x1, exp1, abs_tol=1e-3)
        assert isclose(x2, exp2, abs_tol=1e-3)


# Тестируем особые случаи
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        solution(0, 2, 3)


def test_complex_coefficients():
    with pytest.raises(TypeError):
        solution(1 + 2j, 2, 3)
