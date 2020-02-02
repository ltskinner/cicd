import unittest

from boneless.subpackage import sub_module_function


class TestSubmodule(unittest.TestCase):
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

    def test_submodule(self):
        res = sub_module_function()
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
