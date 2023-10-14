#This unit test tests the cases of a spring constant with a known (real) value,
#as well as the two main cases that would give errors/non physical results
#(zero mass and zero displacement.) This should cover all possible
#use cases of the function.

import unittest
from spring_const_graph import calculate_spring_constants

class SpringConstantTest(unittest.TestCase):
    def test_spring_constant_with_known_values(self):
        """Tests the spring_constant function with known values."""

        masses = [1.0]  # kilograms
        displacement = [0.01]  # meters

        expected_spring_constant = 9.81  # Newtons per meter

        actual_spring_constant = calculate_spring_constants(masses, displacement)

        self.assertAlmostEqual(expected_spring_constant, actual_spring_constant, places=2)

    def test_spring_constant_with_zero_displacement(self):
        """Tests the spring_constant function with a zero displacement."""

        masses = [1.0]  # kilograms
        displacement = [0.0]  # meters

        expected_spring_constant = None  # Use None for problematic data

        actual_spring_constant = calculate_spring_constants(masses, displacement)

        self.assertEqual(expected_spring_constant, actual_spring_constant)

    def test_spring_constant_with_zero_mass(self):
        """Tests the spring_constant function with a zero mass."""

        masses = [0.0]  # kilograms
        displacement = [0.01]  # meters

        expected_spring_constant = None  # Use None for problematic data

        actual_spring_constant = calculate_spring_constants(masses, displacement)

        self.assertEqual(expected_spring_constant, actual_spring_constant)

if __name__ == '__main__':
    unittest.main()
