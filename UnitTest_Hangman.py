# >>>>>>>>>>>>>>>>>>> Unit Test <<<<<<<<<<<<<<<<<<<<<<
import unittest
import Hangman

class TestHangman(unittest.TestCase):

    def test_GetRandomWord(self):
        random_string = Hangman.Hangman().GetRandomWord()
        self.assertNotIn(random_string, "")

    def test_GetLives(self):
        lives = Hangman.Hangman().GetUserLives("Hangman")
        self.assertGreater(lives, 0)

    def test_IsAllSpacesFilled(self):
        result = Hangman.Hangman().IsAllSpacesFilled("Hangman")
        self.assertTrue(result, True)
    
    def test_IsNotAllSpacesFilled(self):
        result = Hangman.Hangman().IsAllSpacesFilled("Ha_gman")
        self.assertFalse(result, True)

    def test_FillBlankSpaces(self):
        result = Hangman.Hangman().FillBlankSpaces("ATCH", "M", "MATCH", "_ATCH") #MATCH
        self.assertEquals(result, "M A T C H ")

if __name__ == '__main__':
    unittest.main()