import unittest
import pandas as pd

import boneless


class TestUnitBackend(unittest.TestCase):
    def test_order_pizza(self):
        response = boneless.backend.order_pizza()
        #expected_response = "YA PIZZA WAT U WANT"
        expected_response = "deliberate break"
        self.assertEqual(response, expected_response)
    
    def test_get_min_drink_size(self):
        expected_col = 'size'
        expected_answer = '1_size'
        not_expected_answer = '2_size'
        arbitrary_df_only_for_testing_operations = pd.DataFrame({
            expected_col: [expected_answer, not_expected_answer]
        })

        result = boneless.backend.get_min_drink_size(
            arbitrary_df_only_for_testing_operations
        )
        self.assertEqual(result, expected_answer)
