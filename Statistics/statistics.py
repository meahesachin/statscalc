from Calculator.calculator import Calculator
from Statistics.SampleMean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, nums):
        self.data = mean(nums)
        return self.data

    def median(self, nums):
        self.data = median(nums)
        return self.data

    def mode(self, nums):
        self.data = mode(nums)
        return self.data

    def variance(self, nums):
        self.data = variance(nums)
        return self.data
