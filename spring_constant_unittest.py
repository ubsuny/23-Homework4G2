"""
This module contains unit tests for the spring_constant function.

The `SpringConstantTest` class is designed to test the behavior of the `calculate_spring_constants`
function when provided with known input values. The tests check whether the function correctly
calculates the spring constant given mass and displacement values.

Example:
    To run the tests, execute this module directly or use a test runner like `unittest.main()`.

"""
import unittest
from spring_const_graph import calculate_spring_constants

class SpringConstantTest(unittest.TestCase):
    """Unit tests for the spring_constant function."""
    def test_spring_constant_with_known_values(self):
        """Tests the spring_constant function with known values."""
        masses = [1.0]  # kilograms
        displacement = [1.0]  # meters
        expected_spring_constant = 9.81  # Newtons per meter
        actual_spring_constant = calculate_spring_constants(masses, displacement)
        self.assertAlmostEqual(expected_spring_constant, actual_spring_constant, places=2)
if __name__ == '__main__':
    unittest.main()
