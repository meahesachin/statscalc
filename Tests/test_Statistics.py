import unittest
from Calculator import calculator
from Statistics.statistics import Statistics
from CsvReader.CSVReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.stats = Statistics()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.stats, Statistics)

    def test_SampleMean(self):
        my_list = [1, 2, 3, 4]
        self.assertEqual(self.stats.mean(my_list), '2.500000000')

    def test_SampleMedian(self):
        my_list = [1, 2, 3, 4]
        self.assertEqual(self.stats.median(my_list), '2.500000000')

    def test_Mode(self):
        my_list = [4, 1, 2, 2, 3, 5]
        self.assertEqual(self.stats.mode(my_list), [2])
"""

    def test_addition(self):
        test_data = CsvReader("Tests/testdata/UnitTestAddition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(float(row['Value 2']), float(row['Value 1'])), result)

    def test_subtraction(self):
        test_data = CsvReader("Tests/testdata/UnitTestSubtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(float(row['Value 2']), float(row['Value 1'])), result)

    def test_results_property(self):
        self.calculator.add(2, 1)
        self.assertEqual(self.calculator.result, 3)

    def test_multiply(self):
        test_data = CsvReader("Tests/testdata/UnitTestMultiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(float(row['Value 2']), float(row['Value 1'])), result)

    def test_divide(self):
        test_data = CsvReader("Tests/testdata/UnitTestDivision.csv").data
        for row in test_data:
            result = format(float(row['Result']), '.9f')
            # print('Result is: ' + result)
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), result)

    def test_dividebyzero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 1,0)
        # self.assertEqual(self.calculator.divide(6, 0), 0)

    def test_square(self):
        test_data = CsvReader("Tests/testdata/UnitTestSquare.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)

    def test_sqrt(self):
        test_data = CsvReader("Tests/testdata/UnitTestSquareRoot.csv").data
        for row in test_data:
            fmt = ".8f"
            result = float(row['Result'])
            if float(result).is_integer():
                fmt = ".1f"
            result = format(float(row['Result']), fmt)
            self.assertEqual(self.calculator.sqrt(row['Value 1']), result)

"""

if __name__ == '__main__':
    unittest.main()
