import unittest
from seminar11.prime import is_prime


class TestPrime(unittest.TestCase):

    def testPrimeWhitebox(self):
        self.assertFalse(is_prime(-2))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(13))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))
        self.assertTrue(is_prime(97))

    def testPrimeBlackBox(self):
        self.assertFalse(is_prime(-11))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
