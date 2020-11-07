
from Statistics.RandomNumberNoSeed import randomnumbernoseed
from Statistics.RandomNumberWithSeed import randomnumberwithseed
from Statistics.getSeed import getseed
from Statistics.ListofNumWithSeed import listofNumWithSeed
from Statistics.SelectRandItemFromList import selectRandomItemFromList
from Statistics.SelectRandomItemFromListwithSeed import selectRandomItemFromListwithSeed
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

    def selectRandomItemFromList(self,a, b):
        list = self.ListofNumWithSeed(a, b)
        self.result = selectRandomItemFromList(list)
        return list, self.result

    def selectRandomItemFromListwithSeed(self, a, b):

        repeatslist = self.ListofNumWithSeed(0, 10)
        'seed = getseed()'
        self.result = selectRandomItemFromListwithSeed(a,b,repeatslist)
        return repeatslist, self.result
