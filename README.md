# xpytile

**Tiling** and **simultaneous resizing** of side-by-side windows _(theoretically not only)_ for Xfce.  


# Purpose
A Python script to auto-tile and to simultaneously resize docked windows for Xfce.  


## Features:
Simultaneous resizing of adjacent windows  
5 different tilers  

Hotkeys for:
 - Tiling and/or simultaneous resizing can be enabled/disabled  
 - Tiling can be triggered manually on demand  
 - Changing tiler  
 - Storing and re-creating current windows layout  
 - Cycling windows  
 - Swap windows  
 - Set/unset window decoration  
 - and more, see below  
 
The tiler can be controlled remotely.  
All settings are workspace specific.  
So for each workspace you can choose independently, if tiling is enabled and which tiler should be used.  
No limit of supported workspaces  
Config-file  
Pure Python, easily hackable  

### New features
Configurable which (CSD) applications should not be (un)decorated.  
Hotkey to focus previously active window  
Can be controlled remotely.  
Dragging a window with the mouse slightly over the left or the top or bottom border of the workspace  
triggers a re-tiling. So the window positions can be changed / swapped by dragging a window.  
Option to set the mouse-cursor in the middle of the new active window, when changed by hotkey.  
&nbsp; &nbsp; _This visual feedback is helpful, especially when the window decoration is turned off._  
Focus can be set to next adjacent window, in the direction of the pressed arrow-key  
Max. number of tiled windows for the currently active tiler can be increased/decreased per hot-key  


# Hotkeys
Hotkeys can be defined in the config-file.  
Most important hotkeys _(full set see config-file)_:  
```Super_L - 1``` &nbsp; &nbsp; &nbsp; &nbsp; tiler - master and stack vertically  
```Super_L - 2``` &nbsp; &nbsp; &nbsp; &nbsp; tiler - vertically  
```Super_L - 3``` &nbsp; &nbsp; &nbsp; &nbsp; tiler - master and stack horizontally  
```Super_L - 4``` &nbsp; &nbsp; &nbsp; &nbsp; tiler - horizontally  
```Super_L - 0``` &nbsp; &nbsp; &nbsp; &nbsp; tiler - maximize  
```Super_L - c``` &nbsp; &nbsp; &nbsp; &nbsp; cycle tiler  
```Super_L - 5``` &nbsp; &nbsp; &nbsp; &nbsp; restore windows layout  
```Super_L - 6``` &nbsp; &nbsp; &nbsp; &nbsp; store windows layout  
```Super_L - ^``` &nbsp; &nbsp; &nbsp; &nbsp; cycle windows  
```Super_L - ESC``` &nbsp; &nbsp; swap current window with top/left-most window  
```Super_L - q``` &nbsp; &nbsp; &nbsp; &nbsp; toggle simultaneous resizing (on/off)  
```Super_L - w``` &nbsp; &nbsp; &nbsp; &nbsp; toggle tiling (on/off)  
```Super_L - y``` &nbsp; &nbsp; &nbsp; &nbsp; toggle window-decoration (on/off) of tiled windows (*)  
```Super_L - a``` &nbsp; &nbsp; &nbsp; &nbsp; shrink width/height of master window  
```Super_L - s``` &nbsp; &nbsp; &nbsp; &nbsp; enlarge width/height of master window  
```Super_L - m``` &nbsp; &nbsp; &nbsp; &nbsp; increment number of max. tiled windows for active tiler  
```Super_L - n``` &nbsp; &nbsp; &nbsp; &nbsp; decrement number of max. tiled windows for active tiler  
```Super_L - arrow``` &nbsp;focus next adjacent window in the given direction  
```Super_L - b``` &nbsp; &nbsp; &nbsp; &nbsp; focus previously active window  
```Super_L - .``` &nbsp; &nbsp; &nbsp; &nbsp; log name & tile of active window in ```/tmp/xpytile_<USERNAME>.log```  
```Super_L - -``` &nbsp; &nbsp; &nbsp; &nbsp; exit  
*) Hint: In XFCE one can resize windows with ```Alt - Right-Click``` and drag,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;which is useful when windows-decorations are turned off  
# Configuration
Well, edit the _hopefully_ self-explanatory config-file xpytilerc
# Installation
Place xpytilerc in XDG_CONFIG_HOME in ~/.config/ or in /etc/ respectively  
ArchLinux - users can install ```xpytile-git``` from the AUR  
# Start
```./xpytile.py```  
or, to let run in background:  ```nohup ./xpytile.py > /dev/null 2>&1 &```
You may want to assign a hotkey.  
In Xfce for example, add a shortcut to xpytile.py with:  
Xfce-Menu -> Settings -> Keyboard -> Application Shortcuts  
# Dependencies
notify-send _(package: notifylib for ArchLinux, libnotify-bin for Debian/Ubuntu)_  
python3, python-xlib
# Bugs
I'm currently not aware of a bug.  
However, when the program crashes it writes traceback info in ```/tmp/xpytile_<USERNAME>.log```  
# License
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
# Questions
*(Q)* Are gaps supported?  
*(A)* Nope, but you could use an Xfce theme with gaps.  

*(Q)* Does xpytile support multiple monitor setups?  
*(A)* On workspaces that span multiple monitors, simultaneous resizing works fine, tiling not really.  
 
*(Q)* How do I get the exact name and title of a window I want xpytile to ignore?  
*(A)* Run xpyile with -v _or -vv_  or use the hotkey to log name and title of the current window.  

*(Q)* What can I do, xptile isn't picking up my hotkeys?  
*(A)* Run ```./getModifierCode.py```, press ```Super_L - 1``` _(or the modifier you'd like to use)_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and check/edit ```xpytilerc``` _(line: modifier = )_  

*(Q)* I'm running out of hotkeys, what can I do?  
*(A)* xpytile can be controlled remotely, consider making a dmenu or rofi script.  
