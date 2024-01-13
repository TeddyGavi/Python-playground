import unittest
from lotide.eq_objects import eq_objects


class TestEqObjects(unittest.TestCase):
    def test_eq_objects(self):
        """
        Test that eq_objets returns true, given two eq eq_objects
        """
        result = eq_objects({"a": {"c": 2}, "b": 1}, {"a": {"c": 2}, "b": 1})
        self.assertTrue(result, f"Expected true, but got {result}")

    def test_eq_objects_nulls(self):
        result = eq_objects({}, None)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
