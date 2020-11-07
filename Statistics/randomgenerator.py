import random
from Statistics.RandomNumberNoSeed import randomnumbernoseed
from Statistics.RandomNumberWithSeed import randomnumberwithseed
from Statistics.getSeed import getseed
from Statistics.ListofNumWithSeed import listofNumWithSeed
class RandomGenerator:
    def __init__(self):
        pass

    def GenRandNumNoSeed(self, a , b):
        self.result = randomnumbernoseed(a, b)
        return self.result

    def GenRandNumWithSeed(self, a, b):
        seed = getseed()
        self.result = randomnumberwithseed(a,b ,seed)
        return self.result
    def getSeed(self):
        self.result = getseed()
        return self.result
    def ListofNumWithSeed(self, a, b):
        seed = getseed()
        self.result = listofNumWithSeed(a,b, seed)
        return self.result