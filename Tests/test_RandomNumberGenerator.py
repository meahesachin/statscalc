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
    def test_GenRandNumWithSeed(self):
        result = self.randomgenerator.GenRandNumWithSeed(0, 255)
        pprint(result)

    def test_ListofNumWithSeed(self):
        result = self.randomgenerator.ListofNumWithSeed(0, 10)
        pprint(result)
    def test_selectRandomItemFromList(self):
        result = self.randomgenerator.selectRandomItemFromList(0, 10)
        pprint(result)

    def test_selectRepeatRandomItemFromList(self):
        result = self.randomgenerator.selectRandomItemFromListwithSeed(0, 5)
        pprint(result)