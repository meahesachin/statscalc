from Calculator.calculator import Calculator
from Statistics.ListofNumWithSeed import listofNumNoSeed
from Statistics.SimpleRandomSampling import simple_rand_sampling
from Statistics.Confidence_Interval import confidence_intervalUpper, confidence_intervalLower
from Statistics.MarginOfError import margin_of_error
class PopulationSampling(Calculator):
    def __init__(self):
        pass

    def simple_random_sampling(self, a, b, N):
        sample = listofNumNoSeed(a, b)
        self.result = simple_rand_sampling(sample, N)
        return sample, self.result

    def confidence_interval(self,a,b,z, N):
        data = listofNumNoSeed(a, b)
        sample = simple_rand_sampling(data, N)
        self.upper = confidence_intervalUpper(sample, z,N)
        self.lower = confidence_intervalLower(sample, z,N)


        return sample, self.lower, self.upper

    def margin_of_error(self, a,b,z,N):
        data = listofNumNoSeed(a, b)
        sample = simple_rand_sampling(data, N)
        self.result = margin_of_error(sample,z,N)
        return sample, self.result