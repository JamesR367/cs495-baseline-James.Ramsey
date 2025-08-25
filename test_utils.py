import unittest
import utils


class AlternatingLettersTests(unittest.TestCase):
    def test_AlternatingLetters_lowercase(self):
        self.assertEqual(utils.AlternatingLetters("baton rouge"), "BaToN RoUgE")

    def test_AlternatingLetters_uppercase(self):
        self.assertEqual(utils.AlternatingLetters("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), "ThE QuIcK BrOwN FoX JuMpS OvEr tHe lAzY DoG")

    def test_AlternatingLetters_mixed(self):
        self.assertEqual(utils.AlternatingLetters("12345This Class Is Cool"), "12345tHiS ClAsS Is cOoL")


if __name__ == "__main__":
    unittest.main()