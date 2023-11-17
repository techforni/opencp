import unittest

from core.statistic import average

class TestStatisticFunc(unittest.TestCase):
    def tesAverage(self):
        mockData = [7, 8, 7.5]
        r = average(mockData)
        self.assertEqual(r, 7.5)