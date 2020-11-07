import random

def selectRandomItemFromListwithSeed(a,b,repeatslist):

    repeats= []
    for i in range(a, b):
        'random.seed(seed)'
        n = random.choice(repeatslist)
        repeats.append(n)
    return repeats
