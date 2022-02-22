import unittest
import Browser as main


class MyTestCase(unittest.TestCase):
    def test_ite(self):
        main.url = 'http://www.ite.edu.sg/'


if __name__ == '__main__':
    unittest.main()
