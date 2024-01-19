# test_calculators.py
import unittest
from src.calculators.combinations import calculate_combinations

class TestCalculators(unittest.TestCase):
    def test_combinations(self):
        self.assertEqual(calculate_combinations(5, 3), 10)
        # Add more tests...

if __name__ == '__main__':
    unittest.main()
