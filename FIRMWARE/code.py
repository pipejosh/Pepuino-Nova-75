print("Starting")
print("Impboard")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


encoder = EncoderHandler()
keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules = [encoder]
keyboard.col_pins = (board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20)
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [

    [ KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL, KC.MPLY, 
      KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.HOME, 
      KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.PGUP, 
      KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.NO, KC.PGDN,    
      KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLASH, KC.NO, KC.RSFT, KC.UP, KC.END,
      KC.LCTRL, KC.LWIN, KC.LALT, KC.NO, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.RALT, KC.RWIN, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT]
    
]

encoder.pins = (board.GP21, board.GP22, None)
encoder.map = [ 

    (KC.A, KC.B)
]







if __name__ == '__main__':
    keyboard.go()