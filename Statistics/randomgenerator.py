import random
from Statistics.RandomNumberNoSeed import randomnumbernoseed
class RandomGenerator:
    def GenRandNumNoSeed(self, a , b):
        self.result = randomnumbernoseed(a, b)
        return self.result