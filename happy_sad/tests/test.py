import unittest
import importlib
from unittest.mock import Mock

import microbit as mbit

# The SUT.
import script

class TestScript(unittest.TestCase):

    def setUp(self):
        # Start every test with clean mocks.
        global mbit
        mbit = importlib.reload(mbit)

    def tearDown(self):
        pass

    def test_no_image_shown_without_button_presses(self):
        script.step()
        script.step()
        script.step()
        self.assertFalse(mbit.display.show.called)

    def test_happy_face_shown_on_button_a_press(self):
        mbit.button_a.is_pressed.return_value = True
        script.step()
        mbit.display.show.called_with(mbit.Image.HAPPY)

    def test_sad_face_shown_on_button_b_press(self):
        mbit.button_b.is_pressed.return_value = True
        script.step()
        mbit.display.show.called_with(mbit.Image.SAD)
