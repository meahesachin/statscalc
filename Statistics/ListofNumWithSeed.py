import random
from Statistics.RandomNumberWithSeed import randomnumberwithseed
def listofNumWithSeed(a, b, seed):
    random.seed(seed)
    list = []
    for i in range(a, b):
        n = random.randint(0, 255)
        list.append(n)
    return list