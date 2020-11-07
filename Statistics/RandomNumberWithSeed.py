import random

def randomnumberwithseed(a ,b, seed):
    random.seed(seed)
    return random.randint(a, b)
