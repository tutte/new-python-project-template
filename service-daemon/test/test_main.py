import src
import unittest

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(src.main(), 0)