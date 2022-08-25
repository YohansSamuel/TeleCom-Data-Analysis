import sys
import os
import unittest
import numpy as np
import pandas as pd


sys.path.insert(0, '../scripts/')
sys.path.append(os.path.abspath(os.path.join('scripts')))

from data_cleaning import DataCleaning

# sample dataframe
df = pd.DataFrame({'numbers': [2, 4, 6, 7, 9], 'letters': ['a', 'b', 'c', 'd', 'e'],
                   'floats': [0.2323, -0.23123, np.NaN, np.NaN, 4.3434]})

class TestCases(unittest.TestCase):
     def test_remove_duplicates(self):
        data_cleaner = DataCleaning(df)
        data_cleaner.remove_duplicates()
        self.assertEqual(data_cleaner.df.shape[0], df.shape[0])


if __name__ == '__main__':
    unittest.main()