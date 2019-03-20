from unittest import TestCase
from RC import *


class TestRC(TestCase):
    def test_replacement_cost(self):
        self.assert_(V_C == -100)

    def test_replacement_cost1(self):
        self.assert_(RC == 0)