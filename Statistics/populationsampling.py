
from Statistics.ListofNumWithSeed import listofNumNoSeed
from Statistics.SimpleRandomSampling import simple_rand_sampling
from Statistics.Confidence_Interval_95 import confidence_interval_95Upper, confidence_interval_95Lower

class PopulationSampling:
    def __init__(self):
        pass

    def simple_random_sampling(self, a, b, N):
        sample = listofNumNoSeed(a, b)
        self.result = simple_rand_sampling(sample, N)
        return sample, self.result

    def confidence_interval_95(self,a,b, N):
        data = listofNumNoSeed(a, b)
        self.upper = confidence_interval_95Upper(data, N)
        self.lower = confidence_interval_95Lower(data, N)


        return self.lower, self.upper