# xpytile

**Tiling** and **simultaneous resizing** of side-by-side windows _(not only)_ for Xfce.
Tested with Xfce, it should work with any window manager compliant to the EWMH standard.


# Purpose
A Python script to auto-tile and to simultaneously resize docked windows.


## Features:
Simultaneous resizing of adjacent windows
5 different tilers
Hotkeys for:
 - Tiling and/or simultaneous resizing can be enabled/disabled
 - Tiling can be triggered manually on demand
 - Changing tiler
 - Storing and re-creating current windows layout
 - Cycling windows
All settings are workspace specific.
So for each workspace you can choose independently,
if tiling is enabled and which tiler should be used. 
No limit of supported workspaces
Config-file
Pure Python, easily hackable


# Hotkeys
Hotkeys can be defined in the config-file.
Most important hotkeys (full set see config-file):
```Super_L - 1``` tiler - master and stack vertically
```Super_L - 2``` tiler - vertically
```Super_L - 3``` tiler - master and stack horizontally
```Super_L - 4``` tiler - horizontally
```Super_L - 0``` tiler - maximize
```Super_L - 5``` restore windows layout
```Super_L - 6``` store windows layout
```Super_L - ^``` cycle windows
```Super_L - q``` toggle simultaneous resizing (on/off)
```Super_L - w``` toggle tiling (on/off)
```Super_L - a``` shrink width/height of master window and (re-)tile
```Super_L - s``` enlarge width/height of master window and (re-)tile
```Super_L - .``` log name & tile of active window in /tmp/xpytile_<USERNAME>.log
```Super_L - -``` exit


# Configuration
Well, edit the (hopefully) self-explanatory config-file xpytile.conf


# Installation
Place xpytilerc in XDG_CONFIG_HOME or in ~/.config/ respectively


# Start
```./xpytile.py``` 
or, to let run in background:  ```nohup ./xpytile.py > /dev/null 2>&1 &```

You may want to assign a hotkey.
In Xfce for example, add a shortcut to xpytile.py
with Xfce-Menu -> Settings -> Keyboard -> Application Shortcuts


# Dependencies
notify-send _(package: notifylib for ArchLinux, notifylib-bin for Debian/Ubuntu)_
python3, python-xlib 

# Bugs
I'm currently not aware of a bug.
When the program crashes, it writes traceback info in /tmp/xpytile_<USERNAME>.log

# Questions
*(Q)* Are gaps supported?
*(A)* Nope
  
*(Q)* Does xpytile support multiple monitor setups?
*(A)* On workspaces that span multiple monitors, simultaneous resizing works fine, tiling not really.

*(Q)* How do I get the exact name and title of a window I want xpytile to ignore?
*(A)* Run xpyile with -v (or -vv)  or use the hotkey to log name and title of the current window.

