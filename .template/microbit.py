#
# This is a module that mocks the original 'microbit' module. Use it for unit
# testing microbit apps on a development host (i. e. non-microbit) environment.
#

from unittest.mock import Mock

# pylint: disable=invalid-name

# Global.
panic = Mock()
reset = Mock()
sleep = Mock()
running_time = Mock(return_value=0)
temperature = Mock(return_value=0)

# Buttons.
button_a = Mock()
button_a.is_pressed.return_value = False
button_a.was_pressed.return_value = False
button_a.get_presses.return_value = 0
button_b = Mock()
button_b.is_pressed.return_value = False
button_b.was_pressed.return_value = False
button_b.get_presses.return_value = 0

# Display.
display = Mock()
display.get_pixel = Mock(return_value=0)

# I/O pins.
pin1 = Mock()
pin1.read_analog.return_value = 0
pin1.is_touched.return_value = False
pin2 = Mock()
pin2.read_analog.return_value = 0
pin2.is_touched.return_value = False
pin3 = Mock()
pin3.read_analog.return_value = 0
pin3.is_touched.return_value = False

# Image.
Image = Mock()

# Accelerometer.
accelerometer = Mock()
accelerometer.get_x.return_value = 0
accelerometer.get_y.return_value = 0
accelerometer.get_z.return_value = 0
accelerometer.get_values.return_value = (0, 0, 0)
accelerometer.current_gesture.return_value = ""
accelerometer.is_gesture.return_value = False
accelerometer.was_gesture.return_value = False
accelerometer.get_gestures.return_value = ()

# Compass.
compass = Mock()
compass.heading.return_value = 0
compass.get_field_strength.return_value = 0
compass.is_calibrated.return_value = True

# I2C.
i2c = Mock()
i2c.read.return_value = None

# UART.
uart = Mock()
uart.any.return_value = False
uart.read.return_value = None
uart.readall.return_value = None
