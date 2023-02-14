import unittest

def is_palindrome(x):

    return x == x[::-1]

class TestStringFunctions(unittest.TestCase):
    
    def test_prepend(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("not"))


if __name__ == "__main__":
    unittest.main()    
