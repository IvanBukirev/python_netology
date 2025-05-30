import unittest

from classes.Tests.unit_tests.tasks_from_the_first_module import vote


class TestVoteFunction(unittest.TestCase):

    def test_clear_winner(self):
        self.assertEqual(vote([1, 1, 1, 2, 3, 3, 3, 3]), 3)
        self.assertEqual(vote([1, 2, 3, 2, 2]), 2)

    def test_tie_breaker(self):
        # При ничье возвращается первый из наиболее частых в порядке появления
        self.assertEqual(vote([1, 2, 3, 1, 2, 3]), 1)
        self.assertEqual(vote(["a", "b", "b", "a", "c"]), "a")
        self.assertEqual(vote([3, 2, 1, 2, 3]), 3)

    def test_single_element(self):
        self.assertEqual(vote([5]), 5)
        self.assertEqual(vote(["test"]), "test")
        self.assertEqual(vote([None]), None)

    def test_negative_numbers(self):
        self.assertEqual(vote([-1, -1, 0, 0, 0]), 0)
        self.assertEqual(vote([10, -5, -5, 10, -5]), -5)

    def test_different_data_types(self):
        self.assertEqual(vote(["apple", "banana", "apple"]), "apple")
        self.assertEqual(vote([True, False, True, True]), True)
        self.assertEqual(vote([1.5, 2.5, 1.5]), 1.5)

    def test_large_input(self):
        large_list = [7] * 1000 + [8] * 500
        self.assertEqual(vote(large_list), 7)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            vote([])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            vote("string")
        with self.assertRaises(TypeError):
            vote(123)
        with self.assertRaises(TypeError):
            vote(None)
        with self.assertRaises(TypeError):
            vote({"a": 1, "b": 2})

    def test_equal_frequency(self):
        # Проверка, что возвращается первый элемент с максимальной частотой
        self.assertEqual(vote([1, 2, 2, 1, 3]), 1)
        self.assertEqual(vote(["z", "y", "x", "y", "z"]), "z")
        self.assertEqual(vote([3, 3, 2, 2, 1, 1, 4]), 3)


if __name__ == '__main__':
    unittest.main()