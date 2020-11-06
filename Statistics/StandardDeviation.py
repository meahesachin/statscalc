
from Statistics.Variance import variance
from Calculator.squareroot import squareroot


def stddev(nums):

    var = variance(nums)
    return squareroot(var)



