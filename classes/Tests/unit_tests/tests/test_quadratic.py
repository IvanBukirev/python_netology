import unittest

from classes.Tests.unit_tests.tasks_from_the_first_module import discriminant, solution


class TestQuadraticEquation(unittest.TestCase):

    # Тесты для функции discriminant`
    def test_discriminant_positive(self):
        self.assertEqual(discriminant(1, -3, 2), 1)  # D = (-3)² - 4*1*2 = 1

    def test_discriminant_zero(self):
        self.assertEqual(discriminant(1, -4, 4), 0)  # D = (-4)² - 4*1*4 = 0

    def test_discriminant_negative(self):
        self.assertEqual(discriminant(3, -4, 2), -8)  # D = (-4)² - 4*3*2 = -8

    # Тесты для функции solution
    def test_no_roots(self):
        self.assertEqual(solution(3, -4, 2), 'корней нет')

    def test_one_root(self):
        self.assertEqual(solution(1, -4, 4), 2.0)  # x = -(-4)/(2*1) = 4/2 = 2

    def test_two_roots(self):
        result = solution(1, -3, 2)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], 2.0)  # x1 = (3 + √1)/2 = 4/2 = 2
        self.assertAlmostEqual(result[1], 1.0)  # x2 = (3 - √1)/2 = 2/2 = 1

    def test_fractional_roots(self):
        result = solution(1, -5, 6)
        self.assertAlmostEqual(result[0], 3.0)  # x1 = (5 + √1)/2 = 6/2 = 3
        self.assertAlmostEqual(result[1], 2.0)  # x2 = (5 - √1)/2 = 4/2 = 2

    def test_negative_roots(self):
        result = solution(1, 4, 3)
        self.assertAlmostEqual(result[0], -1.0)  # x1 = (-4 + √4)/2 = -2/2 = -1
        self.assertAlmostEqual(result[1], -3.0)  # x2 = (-4 - √4)/2 = -6/2 = -3

    def test_zero_a(self):
        with self.assertRaises(ZeroDivisionError):
            solution(0, 2, 3)  # a не может быть 0


if __name__ == '__main__':
    unittest.main()