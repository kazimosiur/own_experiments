import sys
sys.path.insert(-1,'/Users/k.rahman.3/PycharmProjects/own_experiments/unittestcases/dev')

from finding_crazy import find_sum,find_sum_tuple
import unittest
import pandas as pd
from sklearn.utils import check_X_y

class TestSum(unittest.TestCase):

    def test_find_sum(self):
        self.assertEqual(find_sum([1,3,4]), 8)

    def test_find_sum_tuple(self):
        self.assertEqual(find_sum_tuple([1,3,4]), 7)

    def test_data_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

    def test_df_shape(self):
        rand_df = pd.DataFrame([random.sample(range(10, 30), 5) for i in range(10)])
        self.ass

rand_df = pd.DataFrame([random.sample(range(10, 30), 5) for i in range(10)])

check_X_y(rand_df[[0,1,2]],rand_df[1,3])

if __name__ == '__main__':
    # try:
    #     ## if more than one fails you need a test runner here
    #     """
    #         unittest
    #         nose or nose2
    #         pytest
    #     """
    #     test_find_sum()
    #     test_find_sum_tuple()
    # except:
    #     print("tests did not pass")
    unittest.main()