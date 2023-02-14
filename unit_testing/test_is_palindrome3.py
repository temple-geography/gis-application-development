import unittest
from is_palindrome3 import is_palindrome

class TestStringFunctions(unittest.TestCase):
    
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("not"))
        # self.assertTrue(is_palindrome("Was it a cat I saw?"))

if __name__ == "__main__":
    unittest.main()    
