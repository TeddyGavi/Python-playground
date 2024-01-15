import unittest
from lotide.eq_arrays import eq_arrays


class TestEqArrays(unittest.TestCase):
    def test_eq_arrays(self):
        result = eq_arrays(None, [1, 2, 3, 4])
        self.assertFalse(result)

    def test_eq_arrays_true(self):
        result = eq_arrays([1, 2, 3], [1, 2, 3])
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
