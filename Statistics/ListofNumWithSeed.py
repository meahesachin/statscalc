import random
def listofNumWithSeed(a, b, state):
    random.setstate(state)
    list = []
    for i in range(a, b):
        n = random.randint(0, 100)
        list.append(n)
    return list
def listofNumNoSeed(a, b):
    list = []
    for i in range(a, b):
        n = random.randint(0, 100)
        list.append(n)
    return list