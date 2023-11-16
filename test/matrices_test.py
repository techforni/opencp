import unittest

from core.matrices import matrix_sum
from core.matrices import matrix_subtract
from core.matrices import matrix_multiply
from core.matrices import matrix_quotient



class TestMatricesOperations(unittest.TestCase):
    def testSum(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        mockSum = matrix_sum(l1, l2)
        self.assertEqual(mockSum, [5, 7, 9])

    def testSubtract(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        mockSum = matrix_subtract(l1, l2)
        self.assertEqual(mockSum, [-3, -3, -3])

    def testMultiply(self):
        l1 = [0, 0, 0]
        l2 = [4, 5, 6]
        mockSum = matrix_multiply(l1, l2)
        self.assertEqual(mockSum, [0, 0, 0])
        
    def testQuotient(self):
        l1 = [4, 5, 18]
        l2 = [2, 5, 6]
        mockSum = matrix_quotient(l1, l2)
        self.assertEqual(mockSum, [2, 1, 3])