import unittest
from app.src.data_capture import DataCapture
from app.src.stats import Stats

class TestDataCapture(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.capture = DataCapture()

    def test_add_success(self):
        r1, r2, r3 = self.capture.add(0), self.capture.add(10), self.capture.add(999)
        self.assertEqual(r1, None)
        self.assertEqual(r2, None)
        self.assertEqual(r3, None)

    def test_add_fail_on_positive_value(self):
        with self.assertRaises(ValueError):
            self.capture.add(-10)

    def test_add_fail_on_value_greater_or_equal_to_1000(self):
        with self.assertRaises(ValueError):
            self.capture.add(1000)

    def test_add_fail_on_value_not_int(self):
        with self.assertRaises(ValueError):
            self.capture.add('10')

    def test_build_stats_success(self):
        self.capture.add(1)
        self.capture.add(2)
        stats = self.capture.build_stats()
        self.assertIsInstance(stats, Stats)

    def test_build_stats_success_on_empty_data_capture(self):
        stats = self.capture.build_stats()
        self.assertIsInstance(stats, Stats)

    def test_clean(self):
        self.capture.add(1)
        self.capture.add(2)
        r = self.capture.clean()
        self.assertEqual(r, None)

if __name__ == '__main__':
    unittest.main()