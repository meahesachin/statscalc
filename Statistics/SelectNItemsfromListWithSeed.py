import random

def selectNItemsFromListWithSeed(list,N, state):
    random.setstate(state)
    Nitems = random.choices(list,weights=None,cum_weights=None,k=N)

    return Nitems