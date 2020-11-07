import unittest
from Calculator import calculator
from pprint import pprint
from Statistics.populationsampling import PopulationSampling
import random
class PopSamplingTestCase(unittest.TestCase):
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

    def test_Confidence_Intervalfor95(self):
        N = 5
        z =1.960
        result = self.populationsampling.confidence_interval(0,20,z,N)
        pprint("test_Confidence_Intervalfor95")
        pprint(result)


