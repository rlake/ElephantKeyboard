import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.D9, board.D8, board.D7, board.D6, board.D5)
    col_pins = (
        board.SCK,
        board.MISO,
        board.MOSI,
        board.D10,
    )
    diode_orientation = DiodeOrientation.COL2ROW
    i2c = board.I2C
