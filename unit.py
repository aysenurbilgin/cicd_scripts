import unittest
import pandas as pd
import numpy as np

from revenue_processing import process_revenue_loss


class TestsRevenue(unittest.TestCase):

    def __init__(self, test_input_data, test_output_data):
        self.test_input_data = pd.DataFrame(test_input_data)
        self.test_output_data = pd.DataFrame(test_output_data)

    def test_process_revenue_loss(self):
        """
        Test
        """
        actual_output = process_revenue_loss(self.test_input_data, 'Actual')

        test_result = np.alltrue(pd.DataFrame(self.test_output_data).values == pd.DataFrame(actual_output).values)

        assert (test_result)