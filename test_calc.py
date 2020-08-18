'''
    Unit test cases for calculator program
    Importing the calculator module which I have already created
    Importing unittest module
'''
import unittest
import calculator

#Inheriting from unittest.Testcase
class TestCalc(unittest.TestCase):
    def test_add(self):
        '''Test case for addition'''
        self.assertEqual(calculator.add(3, 3), 6)
        self.assertEqual(calculator.add(-1, -2), -3)

    def test_subtract(self):
        '''Test case for subtractiob'''
        self.assertEqual(calculator.subtract(6, 3), 3)
        self.assertEqual(calculator.subtract(-1, -2), 1)

    def test_multply(self):
        '''Test case for multiplication'''
        self.assertEqual(calculator.multply(3, 4), 12)
        self.assertEqual(calculator.multply(-1, 0), 0)

    def test_divide(self):
        '''Test case for division'''
        self.assertEqual(calculator.divide(3, 3), 1)
        self.assertEqual(calculator.divide(-1, -1), 1)

        with self.assertRaises(ValueError):
            calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
  
