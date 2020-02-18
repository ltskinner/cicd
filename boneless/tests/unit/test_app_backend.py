
import unittest

from boneless import (update_unit_count_0,
                      update_unit_count_1,
                      update_unit_count_2)


class TestUnitBackend(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_make_unit_0_callback(self):
        n_clicks = 45
        children = update_unit_count_0(n_clicks)
        self.assertEqual(children[0], f'Unit 0 Votes: {n_clicks}')

    def test_make_unit_1_callback(self):
        n_clicks = 45
        children = update_unit_count_1(n_clicks)
        self.assertEqual(children[0], f'Unit 1 Votes: {n_clicks}')

    def test_make_unit_2_callback(self):
        n_clicks = 45
        children = update_unit_count_2(n_clicks)
        self.assertEqual(children[0], f'Unit 2 Votes: {n_clicks}')
