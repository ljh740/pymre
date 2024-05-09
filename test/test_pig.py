import unittest
from Model.Pig import Pig

class UnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_pig(self):
        p = Pig()
        p.eat()