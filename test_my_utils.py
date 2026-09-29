import random
import statistics
import unittest

import my_utils


class TestMyUtils(unittest.TestCase):
    def test_mean_random(self):
        values = [
            random.randint(-100, 100)
            for _ in range(20)
        ]
        expected = statistics.mean(values)

        self.assertEqual(my_utils.find_mean(values), expected)

    def test_mean_positive(self):
        values = [10, 20, 30]

        self.assertEqual(my_utils.find_mean(values), 20)

    def test_mean_negative(self):
        values = [-10, -20, -30]

        self.assertEqual(my_utils.find_mean(values), -20)

    def test_median_random(self):
        values = [
            random.randint(-100, 100)
            for _ in range(20)
        ]
        expected = statistics.median(values)

        self.assertEqual(my_utils.find_median(values), expected)

    def test_median_positive(self):
        values = [10, 20, 30]

        self.assertEqual(my_utils.find_median(values), 20)

    def test_median_negative(self):
        values = [-10, -20, -30]

        self.assertEqual(my_utils.find_median(values), -20)

    def test_std_random(self):
        values = [
            random.randint(-100, 100)
            for _ in range(20)
        ]
        expected = statistics.pstdev(values)

        self.assertAlmostEqual(my_utils.find_std(values), expected)

    def test_std_positive(self):
        values = [10, 20, 30]
        expected = statistics.pstdev(values)

        self.assertAlmostEqual(my_utils.find_std(values), expected)

    def test_std_negative(self):
        values = [-10, -20, -30]
        expected = statistics.pstdev(values)

        self.assertAlmostEqual(my_utils.find_std(values), expected)


if __name__ == "__main__":
    unittest.main()
