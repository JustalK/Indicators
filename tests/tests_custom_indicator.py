import unittest
import init

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertTrue(1 == 1)
        initialisation = init.Init()
        #initialisation.start()

if __name__ == '__main__':
    unittest.main()
