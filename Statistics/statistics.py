from Calculator.calculator import Calculator
from Statistics.SampleMean import mean


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, nums):
        self.data = mean(nums)
        return self.data
