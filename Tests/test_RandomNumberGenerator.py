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
        pprint("test_GenRandNumNoSeed ")
        pprint(result)
    def test_GenRandNumWithSeed(self):
        self.randomgenerator.getSeed()
        state = random.getstate()
        result = self.randomgenerator.GenRandNumWithSeed(0, 255, state)
        result2 = self.randomgenerator.GenRandNumWithSeed(0, 255, state)
        self.assertEqual(result, result2)
        pprint("test_GenRandNumWithSeed ")
        pprint(result)
        pprint(result2)


    def test_ListofNumWithSeed(self):
        self.randomgenerator.getSeed()
        state = random.getstate()
        result = self.randomgenerator.ListofNumWithSeed(0, 10, state)
        result2 = self.randomgenerator.ListofNumWithSeed(0, 10, state)
        self.assertEqual(result, result2)
        pprint("test_ListofNumWithSeed ")
        pprint(result)
        pprint(result2)

    def test_selectRandomItemFromList(self):
        self.randomgenerator.getSeed()
        state = random.getstate()
        result = self.randomgenerator.selectRandomItemFromList(0, 10, state)
        result2 = self.randomgenerator.selectRandomItemFromList(0, 10, state)
        self.assertEqual(result, result2)
        pprint("test_selectRandomItemFromList ")
        pprint(result)
        pprint(result2)

    def test_selectRepeatRandomItemFromList(self):
        self.randomgenerator.getSeed()
        state = random.getstate()
        result = self.randomgenerator.selectRandomItemFromListwithSeed(0, 5, state)
        result2 = self.randomgenerator.selectRandomItemFromListwithSeed(0, 5, state)
        self.assertEqual(result, result2)
        pprint("test_selectRepeatRandomItemFromList ")
        pprint(result)
        pprint(result2)

    def test_selectNitemsFromListNoSeed(self):
        N = 3
        result = self.randomgenerator.selectNitemsFromListNoSeed(0,10,N)
        pprint("test_selectNitemsFromListNoSeed ")
        pprint(result)

    def test_selectNitemsFromListWithSeed(self):
        N= 3
        self.randomgenerator.getSeed()
        state = random.getstate()
        result = self.randomgenerator.selectNitemsFromListWithSeed(0,10,N, state)
        result2 = self.randomgenerator.selectNitemsFromListWithSeed(0, 10, N, state)
        self.assertEqual(result, result2)
        pprint("test_selectNitemsFromListWithSeed ")
        pprint(result)
        pprint(result2)
