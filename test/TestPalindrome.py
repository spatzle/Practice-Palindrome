import unittest

from PalindromeRunner import Palindrome

class TestPalindrome(unittest.TestCase):
    
    def testPalindromeLenIsOdd(self):
        p = Palindrome("racecar")
        q = Palindrome("abba")
        self.assertTrue(p.lenIsOdd())
        self.assertFalse(q.lenIsOdd())
        
 

if __name__ == '__main__':
    unittest.main()