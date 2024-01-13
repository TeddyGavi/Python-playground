import unittest
from lotide import count_letters


class TestCountLetters(unittest.TestCase):
    def test_count_letters(self):
        self.assertEqual(
            count_letters.count_letters("hello"), {"h": 1, "e": 1, "l": 2, "o": 1}
        )

    def test_count_letters_second(self):
        self.assertNotEqual(
            count_letters.count_letters("hello"),
            {"e": 1, "l": 2, "o": 1},
        )


if __name__ == "__main__":
    unittest.main()
