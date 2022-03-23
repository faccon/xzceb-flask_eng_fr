import unittest
from ..translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_translation(self):
        """ Testing for translation """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_null_input(self):
        self.assertIsNone(english_to_french(None))

class TestFrenchToEnglish(unittest.TestCase):
    def test_translation(self):
        """ Testing for translation """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test_null_input(self):
        self.assertIsNone(french_to_english(None))

unittest.main()
