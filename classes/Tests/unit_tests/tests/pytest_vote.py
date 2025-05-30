import pytest

from classes.Tests.unit_tests.tasks_from_the_first_module import vote

# Тестируемые случаи
TEST_CASES = [
        # Один явный победитель
        ([1, 1, 1, 2, 3, 3, 3, 3], 3),
        ([1, 2, 3, 2, 2], 2),

        # Ничья - возвращается первый из наиболее частых
        ([1, 2, 3, 1, 2, 3], 1),
        (["a", "b", "b", "a", "c"], "a"),

        # Один элемент
        ([5], 5),

        # Отрицательные числа и ноль
        ([-1, -1, 0, 0, 0], 0),
        ([10, -5, -5, 10, -5], -5),

        # Строки и разные типы данных
        (["apple", "banana", "apple"], "apple"),
        ([True, False, True, True], True),

        # Большой массив
        ([7] * 1000 + [8] * 500, 7),
]


# Параметризованный тест
@pytest.mark.parametrize("votes, expected", TEST_CASES)
def test_vote(votes, expected):
    assert vote(votes) == expected


# Тест на пустой ввод
def test_empty_input():
    with pytest.raises(ValueError):
        vote([])


# Тест на неверный тип данных
def test_invalid_input():
    with pytest.raises(TypeError):
        vote("invalid string")
    with pytest.raises(TypeError):
        vote(None)