import unittest
from Calculator import calculator
from pprint import pprint
from Statistics.randomgenerator import RandomGenerator
import random
class RNGTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.randomgenerator = RandomGenerator()

    def test_instantiate_randomgenerator(self):
        randomgenerator = RandomGenerator()
        self.assertIsInstance(randomgenerator, RandomGenerator)

    def test_GenRandNumNoSeed(self):
        result = self.randomgenerator.GenRandNumNoSeed(0, 255)
        pprint(result)