

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
    

if __name__ == '__main__':
    unittest.main()
