import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal

import boneless


class TestIntegrationBackend(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        drinks_fixture_path = './tests/integration/fixtures/drinks.csv'
        self.drinks_df = pd.read_csv(drinks_fixture_path)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_get_drink_sizes(self):
        query = 'limit 10'
        drinks_df = boneless.backend.get_drink_sizes(query)
        assert_frame_equal(drinks_df, self.drinks_df)
