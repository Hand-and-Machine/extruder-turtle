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
G1 Z1
G1 X100 Y0 Z0 E20.0
G1 Z10
G1 X1.2246467991473533e-15 Y20.0 Z0.0
G1 Z-10
G1 Z1
G1 X-100.0 Y1.2246467991473532e-14 Z0.0 E20.0
G1 Z10
G1 X1.2246467991473533e-15 Y20.0 Z0.0
G1 Z-10
G1 Z1
G1 X100.0 Y0.0 Z0.0 E20.0

; FINALIZATION SEQUENCE
M104 S0                 ; cool down hotend
M140 S0                 ; cool down bed
M107                    ; turn off fan
G1 Z100                 ; move extruder above print
M84                     ; disable motors

