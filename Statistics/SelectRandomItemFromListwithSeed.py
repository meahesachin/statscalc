import random

def selectRandomItemFromListwithSeed(a,b,repeatslist, state):

    repeats= []
    for i in range(a, b):
        random.setstate(state)
        n = random.choice(repeatslist)
        repeats.append(n)
    return repeats
