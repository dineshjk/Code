"""
Test suite for input/output utilities.
Tests all functions from Utils.inout module with various scenarios.
"""

import sys
import os
import unittest
from unittest.mock import patch
import io

# Add parent directory to Python path to find Utils package
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Utils import (
    get_integer,
    get_float,
    get_complex,
    get_bunch_integers,
    get_bunch_floats,
    get_bunch_complex
)

class TestInputOutput(unittest.TestCase):
    """Test cases for input/output functions."""

    def setUp(self):
        """Set up test environment."""
        self.test_list = []
        self.held, sys.stdout = sys.stdout, io.StringIO()
        # Ensure we have a clean list for each test
        self.test_list.clear()

    def tearDown(self):
        """Clean up test environment."""
        # Restore stdout
        sys.stdout = self.held

    def test_get_integer(self):
        """Test integer input with various constraints."""
        # Test normal integer input
        with patch('builtins.input', return_value='42'):
            self.assertEqual(get_integer(), 42)

        # Test positive constraint
        with patch('builtins.input', return_value='5'):
            self.assertEqual(get_integer("positive"), 5)

        # Test negative constraint
        with patch('builtins.input', return_value='-5'):
            self.assertEqual(get_integer("negative"), -5)

        # Test range constraints
        with patch('builtins.input', return_value='7'):
            self.assertEqual(get_integer(range_min=1, range_max=10), 7)

        # Test invalid input
        with patch('builtins.input', return_value='abc'):
            with self.assertRaises(ValueError):
                get_integer()

    def test_get_float(self):
        """Test float input with various constraints."""
        # Test normal float input
        with patch('builtins.input', return_value='3.14'):
            self.assertAlmostEqual(get_float(), 3.14)

        # Test positive constraint
        with patch('builtins.input', return_value='2.5'):
            self.assertAlmostEqual(get_float("positive"), 2.5)

        # Test negative constraint
        with patch('builtins.input', return_value='-2.5'):
            self.assertAlmostEqual(get_float("negative"), -2.5)

        # Test range constraints
        with patch('builtins.input', return_value='0.5'):
            self.assertAlmostEqual(get_float(range_min=0.0, range_max=1.0), 0.5)

        # Test invalid input
        with patch('builtins.input', return_value='abc'):
            with self.assertRaises(ValueError):
                get_float()

    def test_get_complex(self):
        """Test complex number input."""
        # Test normal complex input
        with patch('builtins.input', return_value='3+4j'):
            self.assertEqual(get_complex(), 3+4j)

        # Test real-only input
        with patch('builtins.input', return_value='5'):
            self.assertEqual(get_complex(), 5+0j)

        # Test negative imaginary
        with patch('builtins.input', return_value='1-2j'):
            self.assertEqual(get_complex(), 1-2j)

        # Test invalid input
        with patch('builtins.input', return_value='abc'):
            with self.assertRaises(ValueError):
                get_complex()

    def test_get_bunch_integers(self):
        """Test multiple integer input."""
        # Test fixed count input
        inputs = ['1', '2', '3']
        with patch('builtins.input', side_effect=inputs) as mock_input:
            with patch('msvcrt.kbhit', return_value=True):  # Mock kbhit to always return True
                with patch('Utils.keyboard_utils.get_single_key', return_value='\n'):
                    result = get_bunch_integers(self.test_list, n=3)
                    self.assertEqual(result, [1, 2, 3])

        # Test stop on non-integer
        inputs = ['1', '2', 'abc']
        with patch('builtins.input', side_effect=inputs):
            with patch('msvcrt.kbhit', return_value=True):  # Mock kbhit to always return True
                with patch('Utils.keyboard_utils.get_single_key', return_value='\n'):
                    result = get_bunch_integers([], n=None)
                    self.assertEqual(result, [1, 2])

    def test_get_bunch_floats(self):
        """Test multiple float input."""
        # Test fixed count input
        inputs = ['1.1', '2.2', '3.3']
        with patch('builtins.input', side_effect=inputs):
            with patch('msvcrt.kbhit', return_value=True):  # Mock kbhit to always return True
                with patch('Utils.keyboard_utils.get_single_key', return_value='\n'):
                    result = get_bunch_floats(self.test_list, n=3)
                    self.assertEqual(result, [1.1, 2.2, 3.3])

        # Test stop on non-float
        inputs = ['1.1', '2.2', 'abc']
        with patch('builtins.input', side_effect=inputs):
            with patch('msvcrt.kbhit', return_value=True):  # Mock kbhit to always return True
                with patch('Utils.keyboard_utils.get_single_key', return_value='\n'):
                    result = get_bunch_floats([], n=None)
                    self.assertEqual(result, [1.1, 2.2])

    def test_get_bunch_complex(self):
        """Test multiple complex number input."""
        # Test multiple complex numbers
        inputs = ['1+2j', '3-4j', '5']
        with patch('builtins.input', side_effect=inputs):
            with patch('msvcrt.kbhit', return_value=True):  # Mock kbhit to always return True
                with patch('Utils.keyboard_utils.get_single_key', return_value='\n'):
                    result = get_bunch_complex(3)
                    self.assertEqual(result, [1+2j, 3-4j, 5+0j])

        # Test invalid input handling
        inputs = ['1+2j', 'invalid', '3+4j', '5+6j']
        with patch('builtins.input', side_effect=inputs):
            with patch('msvcrt.kbhit', return_value=True):  # Mock kbhit to always return True
                with patch('Utils.keyboard_utils.get_single_key', return_value='\n'):
                    result = get_bunch_complex(3)
                    self.assertEqual(result, [1+2j, 3+4j, 5+6j])

        # Test invalid num_values
        with self.assertRaises(ValueError):
            get_bunch_complex(0)

        # Test single complex number
        inputs = ['1+2j']
        with patch('builtins.input', side_effect=inputs):
            with patch('msvcrt.kbhit', return_value=True):  # Mock kbhit to always return True
                with patch('Utils.keyboard_utils.get_single_key', return_value='\n'):
                    result = get_bunch_complex(1)
                    self.assertEqual(result, [1+2j])

if __name__ == '__main__':
    print("1. Entering main block")
    DEBUG = True

    print("2. Starting test discovery")
    suite = unittest.TestSuite()

    print("3. Adding tests to suite")
    # Add tests in desired order
    suite.addTest(TestInputOutput('test_get_integer'))
    suite.addTest(TestInputOutput('test_get_float'))
    suite.addTest(TestInputOutput('test_get_complex'))
    suite.addTest(TestInputOutput('test_get_bunch_integers'))
    suite.addTest(TestInputOutput('test_get_bunch_floats'))
    suite.addTest(TestInputOutput('test_get_bunch_complex'))

    print("4. Reaching breakpoint")
    if DEBUG:
        # Set breakpoint here
        breakpoint()

    print("5. Starting test execution")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)