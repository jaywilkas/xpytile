#!/usr/bin/env python

from Xlib.display import Display
from Xlib import X


keyCode = 10  # keycode of key '1'

def main():

    disp = Display()
    Xroot = disp.screen().root

    Xroot.change_attributes(event_mask = X.KeyReleaseMask)
    Xroot.grab_key(keyCode, X.AnyModifier, 1, X.GrabModeAsync, X.GrabModeAsync)

    print('Ctrl-C stops program')
    print('Press <any-modifier> 1')

    while True:
        event = Xroot.display.next_event()
        # print(f'event: {event}')
        print(f'keycode: {event.detail}')
        print(f'modifier: {event.state}\n')

if __name__ == '__main__':
    main()
