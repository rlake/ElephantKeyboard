import board

from kb import KMKKeyboard

from kmk.extensions.lock_status import LockStatus
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.handlers.sequences import simple_key_sequence
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

layers_ext = Layers()
keyboard.modules.append(layers_ext)

media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

rgb_ext = RGB(
    pixel_pin=board.A0,
    num_pixels=17,
    val_limit=4,
    val_default=4,
    animation_mode=AnimationModes.BREATHING_RAINBOW
)
keyboard.extensions.append(rgb_ext)

class LEDLockStatus(LockStatus):
    def __init__(self, rgb_ext):
        super().__init__()
        self._rgb_ext = rgb_ext

    def set_lock_leds(self):
        if self.get_num_lock():
            pass
            #leds.set_brightness(50, leds=[0])
            #self._rgb_ext.val = self._rgb_ext.val_default
        else:
            pass
            #self._rgb_ext.val = 0
            #leds.set_brightness(0, leds=[0])

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)
        if self.report_updated:
            self.set_lock_leds()

keyboard.extensions.append(LEDLockStatus(rgb_ext))

num_lock_sequence = simple_key_sequence((KC.NLCK, KC.RGB_TOG))

keyboard.debug_enabled = True

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
    [
        num_lock_sequence,
                 KC.PSLS, KC.PAST, KC.PMNS,
        KC.P7,   KC.P8,   KC.P9,   _______,
        KC.P4,   KC.P5,   KC.P6,   KC.PPLS,
        KC.P1,   KC.P2,   KC.P3,   _______,
        _______, KC.P0, KC.PDOT,   KC.PENT,
        ]
]

if __name__ == '__main__':
    keyboard.go()
