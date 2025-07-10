import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.extensions.LED import LED, AnimationModes

# pins!!!
COL0 = board.D10
COL1 = board.D9
COL2 = board.D8
COL3 = board.D7
ROW0 = board.D3
ROW1 = board.D2

# the LED pin yay
LED_PIN = board.D6

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# breathing LEDS???
led = LED(
    led_pin=[LED_PIN],
    animation_mode=AnimationModes.BREATHING,
    brightness=50
)
keyboard.extensions.append(led)

# Configure matrix pins
keyboard.col_pins = (COL0, COL1, COL2, COL3)
keyboard.row_pins = (ROW0, ROW1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# uhhh
HELLOWORLD = KC.MACRO("Emergency Offline Autotype Message, bye!")

# Define your keymap
keyboard.keymap = [
    [HELLOWORLD,    KC.W,     KC.VOLD,      KC.ESC],
    [KC.A,      KC.S,     KC.D,      KC.DEL]
]

if __name__ == '__main__':
    keyboard.go()
