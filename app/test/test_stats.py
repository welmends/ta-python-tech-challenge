import unittest
from app.src.data_capture import DataCapture
from app.src.stats import Stats


class TestStats(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        self.stats = capture.build_stats()

    def test_constructor(self):
        stats = Stats(1000, [0] * 1000)
        self.assertIsInstance(stats, Stats)

    def test_less_on_success(self):
        r = self.stats.less(4)
        self.assertEqual(r, 2)

    def test_less_on_not_added_value(self):
        r = self.stats.less(10)
        self.assertEqual(r, 5)

    def test_less_on_smallest_added_value(self):
        r = self.stats.less(3)
        self.assertEqual(r, 0)

    def test_less_fail_on_negative_value(self):
        with self.assertRaises(ValueError):
            self.stats.less(-1)

    def test_less_fail_on_value_greater_or_equal_to_1000(self):
        with self.assertRaises(ValueError):
            self.stats.less(1000)

    def test_less_fail_on_value_not_int(self):
        with self.assertRaises(ValueError):
            self.stats.less("10")

    def test_greater_on_success(self):
        r = self.stats.greater(4)
        self.assertEqual(r, 2)

    def test_greater_on_not_added_value(self):
        r = self.stats.greater(2)
        self.assertEqual(r, 5)

    def test_greater_on_biggest_added_value(self):
        r = self.stats.greater(9)
        self.assertEqual(r, 0)

    def test_greater_fail_on_negative_value(self):
        with self.assertRaises(ValueError):
            self.stats.greater(-1)

    def test_greater_fail_on_value_greater_or_equal_to_1000(self):
        with self.assertRaises(ValueError):
            self.stats.greater(1000)

    def test_greater_fail_on_value_not_int(self):
        with self.assertRaises(ValueError):
            self.stats.greater("10")

    def test_between_on_success(self):
        r = self.stats.between(3, 6)
        self.assertEqual(r, 4)

    def test_between_on_equal_values(self):
        r = self.stats.between(4, 4)
        self.assertEqual(r, 1)

    def test_between_on_not_included_values(self):
        r = self.stats.between(2, 100)
        self.assertEqual(r, 5)

    def test_between_on_swapped_lower_and_upper(self):
        r = self.stats.between(6, 3)
        self.assertEqual(r, 4)

    def test_between_fail_on_negative_value(self):
        with self.assertRaises(ValueError):
            self.stats.between(-1, -1)
            self.stats.between(-1, 1)
            self.stats.between(1, -1)

    def test_between_fail_on_value_greater_or_equal_to_1000(self):
        with self.assertRaises(ValueError):
            self.stats.between(1000, 1000)
            self.stats.between(1000, 10)
            self.stats.between(10, 1000)

    def test_between_fail_on_value_not_int(self):
        with self.assertRaises(ValueError):
            self.stats.between("10", "10")
            self.stats.between(10, "10")
            self.stats.between("10", 10)


if __name__ == "__main__":
    unittest.main()
