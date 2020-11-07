import unittest
from Calculator import calculator
from pprint import pprint
from Statistics.populationsampling import PopulationSampling
import random
class RNGTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.populationsampling = PopulationSampling()

    def test_instantiate_populationsampling(self):
        populationsampling = PopulationSampling()
        self.assertIsInstance(populationsampling, PopulationSampling)

    def test_Simple_Random_Sampling(self):
        N= 3
        result = self.populationsampling.simple_random_sampling(0,10,N)
        pprint("test_Simple_Random_Sampling")
        pprint(result)
