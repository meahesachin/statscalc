from Statistics.SampleMean import mean
from Statistics.StandardDeviation import stddev


def zscore(nums):
    mn = mean(nums)
    sd = stddev(nums)
    data = []
    for x in nums:
        z = round((x - float(mn) / float(sd)), 6)
        data.append(z)
    return data

