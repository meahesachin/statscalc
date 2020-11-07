import random

def selectNItemsFromListNoSeed(list,N):

    Nitems = random.choices(list,weights=None,cum_weights=None,k=N)

    return Nitems
