#!/usr/bin/env python3
"""
created: 2022-03-10 19:02:45
@author: seraph★1001100
contact: seraph1001100@gmail.com
project: Temperature Converter
details: Tests Fahrenheit to Celsius and Celsius to Fahrenheit function.
"""

import unittest

from app.temperature_functions import fahrenheit_to_celsius, celsius_to_fahrenheit


class TestSolution(unittest.TestCase):
    """Test temperature conversion function."""

    def test_fahrenheit_to_celsius(self):
        """tests fahrenheit to celsius"""
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertEqual(fahrenheit_to_celsius(0), -17.77777777777778)
        self.assertEqual(fahrenheit_to_celsius(11.15), -11.583333333333334)
        self.assertEqual(fahrenheit_to_celsius(68), 20)
        self.assertEqual(fahrenheit_to_celsius(55), 12.777777777777779)
        self.assertEqual(fahrenheit_to_celsius(-32), -35.55555555555556)
        self.assertEqual(fahrenheit_to_celsius(.0966), -17.72411111111111)
        self.assertEqual(fahrenheit_to_celsius(1003487.003487), 557475.0019372222)
        self.assertEqual(fahrenheit_to_celsius(16), -8.88888888888889)
        self.assertEqual(fahrenheit_to_celsius(-45.63), -43.12777777777777)
        self.assertEqual(fahrenheit_to_celsius(95), 35)
        self.assertEqual(fahrenheit_to_celsius(103.8971), 39.94283333333333)

    def test_celsius_fahrenheit(self):
        """Tests celsius to fahrenheit"""
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(12.32), 54.176)
        self.assertEqual(celsius_to_fahrenheit(45.11), 113.19800000000001)
        self.assertEqual(celsius_to_fahrenheit(-16), 3.1999999999999993)
        self.assertEqual(celsius_to_fahrenheit(176), 348.8)
        self.assertEqual(celsius_to_fahrenheit(20), 68)
        self.assertEqual(celsius_to_fahrenheit(-39.94), -39.891999999999996)
        self.assertEqual(celsius_to_fahrenheit(352.021), 665.6378000000001)
        self.assertEqual(celsius_to_fahrenheit(1776.0001), 3228.8001799999997)
        self.assertEqual(celsius_to_fahrenheit(0.0098564), 32.01774152)


if __name__ == '__main__':
    unittest.main()
