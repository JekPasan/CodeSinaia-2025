import unittest
from TODO_number_to_words import number_to_words

class TestInvalidInputs(unittest.TestCase):
    def test_none(self):
        self.assertEqual(number_to_words(None), None)
    
    def test_non_integer(self):
        self.assertEqual(number_to_words("string"), None)
        self.assertEqual(number_to_words(3.14), None)
        self.assertEqual(number_to_words([]), None)
        self.assertEqual(number_to_words({}), None)
    
    def test_is_in_range(self):
        self.assertEqual(number_to_words(-1), None)
        self.assertEqual(number_to_words(10000), None)

class TestSingleDigits(unittest.TestCase):
    def test_1(self):
        self.assertEqual(number_to_words(1), "one")
    
    def test_2(self):
        self.assertEqual(number_to_words(2), "two")

class TestTeens(unittest.TestCase):
    def test_11(self):
        self.assertEqual(number_to_words(11), "eleven")
    def test_13(self):
        self.assertEqual(number_to_words(13), "thirteen")

class TestTens(unittest.TestCase):
    def test_20(self):

        self.assertEqual(number_to_words(20), "twenty")