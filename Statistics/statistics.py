from Calculator.calculator import Calculator
from Statistics.SampleMean import mean
from Statistics.Median import median


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