#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo remote control script for xpytile

Sends an event with a command number to xpytile.
The list of command-numbers can also be found
in xpytilerc in section hotkeys.



Copyright (C) 2021  jaywilkas  <just4 [period] gmail [at] web [period] de>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import sys
import Xlib.display
import Xlib.X
import Xlib.protocol


# ----------------------------------------------------------------------------------------------------------------------
# no. command
#  0  toggleResize
#  1  toggleTiling
#  2  toggleResizeAndTiling
#  3  toggleMaximizeWhenOneWindowLeft
#  4  toggleDecoration
#  5  cycleWindows
#  6  cycleTiler
#  7  swapWindows
#  8  storeCurrentWindowsLayout
#  9  recreateWindowsLayout
# 10  tileMasterAndStackVertically
# 11  tileVertically
# 12  tileMasterAndStackHorizontally
# 13  tileHorizontally
# 14  tileMaximize
# 15  increaseMaxnumWindows
# 16  decreaseMaxnumWindows
# 17  exit
# 18  logactiveWindow
# 19  shrinkMaster
# 20  enlargeMaster
# 21  focusLeft
# 22  focusRight
# 23  focusUp
# 24  focusDown
# 25  focusPrevious
# ----------------------------------------------------------------------------------------------------------------------


if len(sys.argv) != 2:
    print('missing command number')
    sys.exit(1)

cmd = sys.argv[1]
try:
    cmdNum = int(cmd)
except ValueError:
    print('invalid command number')
    sys.exit(1)


disp = Xlib.display.Display()
screen = disp.screen()
Xroot = screen.root

XPYTILE_REMOTE = disp.intern_atom("_XPYTILE_REMOTE")
data = (32, [cmdNum, 0,0,0,0])

clientMessage = Xlib.protocol.event.ClientMessage(window=Xroot, client_type=XPYTILE_REMOTE, data=data)
mask = mask=(Xlib.X.SubstructureRedirectMask | Xlib.X.SubstructureNotifyMask)
Xroot.send_event(clientMessage, event_mask=mask)
disp.sync()
