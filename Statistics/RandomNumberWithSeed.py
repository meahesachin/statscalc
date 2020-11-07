import random

def randomnumberwithseed(a ,b,state):
    'random.seed(seed)'
    random.setstate(state)
    return random.randint(a, b)
