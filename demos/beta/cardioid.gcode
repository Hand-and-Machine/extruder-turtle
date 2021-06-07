; INITIALIZATION SEQUENCE
G90                     ; absolute coordinates for X,Y,Z axes
M83                     ; relative coordinates for E axis
G21                     ; set units to mm
M104 S215     ; set hotend temperature
M140 S60        ; set bed temperature
M109 S215     ; wait for hotend temperature
M190 S60        ; wait for bed temperature
G28 W                   ; move extruder to home
G80                     ; mesh bed leveling
G1 Y-3 F1000            ; move extruder out of bounds
G1 X60 E9 F1000         ; draw test line
G1 X100 E12.5 F1000     ; draw test line
G92 E0                  ; set E-axis value to zero
G1 X100 Y100            ; go to the origin
G1 F1000          ; set the feedrate
G91                     ; relative coordinates for X,Y,Z axes


G1 F700
