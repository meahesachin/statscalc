
from Statistics.ListofNumWithSeed import listofNumNoSeed
from Statistics.SimpleRandomSampling import simple_rand_sampling

class PopulationSampling:
    def __init__(self):
        pass

    def simple_random_sampling(self, a, b, N):
        sample = listofNumNoSeed(a, b)
        self.result =simple_rand_sampling(sample, N)
        return sample, self.result
