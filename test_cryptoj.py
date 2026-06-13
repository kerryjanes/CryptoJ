# test_cryptoj.py
"""
Tests for CryptoJ module.
"""

import unittest
from cryptoj import CryptoJ

class TestCryptoJ(unittest.TestCase):
    """Test cases for CryptoJ class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoJ()
        self.assertIsInstance(instance, CryptoJ)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoJ()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
