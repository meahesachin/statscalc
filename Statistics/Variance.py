from Statistics.SampleMean import mean
from Calculator.division import division
from Calculator.squared import squared


def variance(nums):

    length = len(nums)
    mn = mean(nums)
    x = 0
    for i in nums:
        x = x + squared(i - float(mn))

    return division(x, length)

