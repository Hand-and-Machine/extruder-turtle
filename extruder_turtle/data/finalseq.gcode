
; FINALIZATION SEQUENCE

G1 E-3 					; Extrude backwards to prevent blob 
M104 S0                 ; cool down hotend
M140 S0                 ; cool down bed
M107                    ; turn off fan
G1 F5000 Z100           ; move extruder above print
M84                     ; disable motors
