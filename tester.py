import unittest
#import week4

from prep import *

class TestProblem(unittest.TestCase):
    
    def test_isPandigital(self):
        self.assertTrue(isPandigital('3421'))
        self.assertTrue(isPandigital('346215'))
        self.assertTrue(isPandigital('21'))
        self.assertTrue(isPandigital('1'))
        
        self.assertFalse(isPandigital('5421'))
        self.assertFalse(isPandigital('3'))
        self.assertFalse(isPandigital('34216'))
        
    
    def test_palindromic(self):
        self.assertTrue(palindromic('1'))
        self.assertTrue(palindromic('22'))
        self.assertTrue(palindromic('134431'))
        self.assertFalse(palindromic('1345'))



if __name__ == '__main__':
    unittest.main()