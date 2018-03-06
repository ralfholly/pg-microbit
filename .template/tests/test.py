import unittest
import importlib
from unittest.mock import Mock

# Mock libs used by SUT.
import microbit as mbit

# The SUT.
import script

class TestScript(unittest.TestCase):

    def setUp(self):
        global mbit
        # Start every test with clean mocks.
        mbit = importlib.reload(mbit)


    def tearDown(self):
        pass


    def test_trivial(self):
        self.assertEqual(3, 2 + 1)
        # TODO:Your tests here...

