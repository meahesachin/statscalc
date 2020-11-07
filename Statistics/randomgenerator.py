
from Statistics.RandomNumberNoSeed import randomnumbernoseed
from Statistics.RandomNumberWithSeed import randomnumberwithseed
from Statistics.getSeed import getseed
from Statistics.ListofNumWithSeed import listofNumWithSeed, listofNumNoSeed
from Statistics.SelectRandItemFromList import selectRandomItemFromList
from Statistics.SelectRandomItemFromListwithSeed import selectRandomItemFromListwithSeed
from Statistics.SelectNItemsfromListNoSeed import selectNItemsFromListNoSeed
from Statistics.SelectNItemsfromListWithSeed import selectNItemsFromListWithSeed
class RandomGenerator:
    def __init__(self):
        pass

    def GenRandNumNoSeed(self, a , b):
        self.result = randomnumbernoseed(a, b)
        return self.result

    def GenRandNumWithSeed(self, a, b, state):
        self.result = randomnumberwithseed(a,b,state)
        return self.result

    def getSeed(self):
        self.result = getseed()
        return self.result

    def ListofNumWithSeed(self, a, b, state):
        self.result = listofNumWithSeed(a,b, state)
        return self.result

    def selectRandomItemFromList(self,a, b, state):
        list = self.ListofNumWithSeed(a, b, state)
        self.result = selectRandomItemFromList(list)
        return list, self.result

    def selectRandomItemFromListwithSeed(self, a, b, state):
        repeatslist = self.ListofNumWithSeed(0, 10, state)
        self.result = selectRandomItemFromListwithSeed(a,b,repeatslist, state)
        return repeatslist, self.result

    def selectNitemsFromListNoSeed(self,a,b, N):
        list = listofNumNoSeed(a, b)
        self.result = selectNItemsFromListNoSeed(list, N)
        return list, self.result

    def selectNitemsFromListWithSeed(self,a,b, N, state):
        list = self.ListofNumWithSeed(a, b, state)
        self.result = selectNItemsFromListWithSeed(list, N, state)
        return list, self.result
