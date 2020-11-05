from Calculator.division import division


def mean(nums):
    length = len(nums)
    total = float(sum(nums))
    return division(total, length)