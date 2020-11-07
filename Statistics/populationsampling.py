
from Statistics.ListofNumWithSeed import listofNumNoSeed
from Statistics.SimpleRandomSampling import simple_rand_sampling
from Statistics.Confidence_Interval import confidence_intervalUpper, confidence_intervalLower

class PopulationSampling:
    def __init__(self):
        pass

    def simple_random_sampling(self, a, b, N):
        sample = listofNumNoSeed(a, b)
        self.result = simple_rand_sampling(sample, N)
        return sample, self.result

    def confidence_interval(self,a,b,z, N):
        data = listofNumNoSeed(a, b)
        self.upper = confidence_intervalUpper(data, z,N)
        self.lower = confidence_intervalLower(data, z,N)


        return self.lower, self.upper