import unittest

# Not neccessary if running from top level
import sys, os
testdir = os.path.dirname(__file__)

sys.path.insert(0, os.path.abspath(os.path.join(testdir, '..')))

from boneless import (module_function,
                      use_sub_module_function,
                      test_read_from_lib)


class TestSum(unittest.TestCase):
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

    def test_module(self):
        res = module_function()
        self.assertTrue(res)

    def test_submodule_import(self):
        res = use_sub_module_function()
        self.assertTrue(res)
    
    def test_test_read_from_lib(self):
        expected = 'ayy lmao'
        returned = test_read_from_lib()
        self.assertEqual(returned, expected)


if __name__ == '__main__':
    unittest.main()
